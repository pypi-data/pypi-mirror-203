"""This module contains all functions related to matrices.
"""
from __future__ import annotations

from itertools import product
from typing import Any, Callable, Dict, List, Set, Tuple

from graphviz import Digraph
from pandas import DataFrame
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components, floyd_warshall

from .set_functions import HashableSet


def dataframe_equals(df1: DataFrame, df2: DataFrame) -> bool:
    """Check if two dataframes have the same values.

    It will realign the indexes and columns if they are ordered differently.

    :param df1:
    :param df2:
    :return:

    .. todo:: integrate into :class:`mcda/core.adjacency_matrix.Matrix`
    """
    return df1.to_dict() == df2.to_dict()


class Matrix:
    """This class implements a wrapper on :class:`pandas.DataFrame`.

    It adds a method to check if two such objects are equals.
    It is meant to be use for any class that needs a DataFrame as its
    internal data representation in this package.

    :param data: dataframe containing the matrix
    """

    def __init__(self, data):
        self.data = DataFrame(data)

    def __mul__(self, other: "Matrix" | float) -> "Matrix":
        """Return product.

        :param other:
        :return:
        """
        coeff = other.data if isinstance(other, Matrix) else other
        return self.__class__(self.data * coeff)

    def __add__(self, other: Any) -> "Matrix":
        """Return addition.

        :param other:
        :return:
        """
        added = other.data if isinstance(other, Matrix) else other
        return self.__class__(self.data + added)

    def __eq__(self, other) -> bool:
        """Check if both matrices have the same dataframe

        :return:

        .. note:: vertices order does not matter
        """
        if type(other) != type(self):
            return False
        return dataframe_equals(self.data, other.data)


class BlockMatrix(Matrix):
    """This class represents a block matrix.

    The block matrix is represented internally by a
    :class:`pandas.DataFrame`.

    Index and column names are all parts of a group, and are formatted as such:
    (`group_label`, `vertex_label`)

    :param data: block matrix in an array-like or dict-structure
    :param row_groups:
    :param column_groups:
    :raise TypeError: if any index or column name is not properly formatted

    .. warning::
        For future compatibility, do not manipulate the indexes directly and
        use :meth:`to_index` and :meth:`from_index` instead.
    """

    def __init__(
        self,
        data,
        row_groups: Dict[Any, List] = None,
        column_groups: Dict[Any, List] = None,
    ):
        index = (
            [
                BlockMatrix.to_index(g, i)
                for g, v in row_groups.items()
                for i in v
            ]
            if row_groups
            else None
        )
        columns = (
            [
                BlockMatrix.to_index(g, i)
                for g, v in column_groups.items()
                for i in v
            ]
            if column_groups
            else None
        )
        data = DataFrame(
            data.values
            if isinstance(data, DataFrame) and row_groups and column_groups
            else data,
            index=index,
            columns=columns,
        )
        super().__init__(data)
        try:
            for index in set(
                self.data.index.tolist() + self.data.columns.tolist()
            ):
                self.from_index(index)
        except TypeError:
            raise TypeError(
                "indexes and columns names must be formatted as groups"
            )

    @classmethod
    def to_index(cls, group: Any, member: Any) -> Any:
        """Return index as formatted internally.

        :param group:
        :param member: vertex part of `group`
        :return:
        """
        return (group, member)

    @classmethod
    def from_index(cls, index: Any) -> Tuple[Any, Any]:
        """Return group and vertex from index.

        :param index:
        :return:
        :raise TypeError: if `index` doesn't respect internal index format
        """
        try:
            group, member = index
            return group, member
        except Exception:
            raise TypeError(f"bad format for 'index': {index}")

    @property
    def row_groups(self) -> Dict[Any, List]:
        """Infer groups from internal `data` indexes

        :return: found groups
        """
        groups: Dict[Any, List] = {}
        for index in self.data.index:
            cat, a = self.from_index(index)
            if cat not in groups:
                groups[cat] = []
            groups[cat].append(a)
        return groups

    @property
    def column_groups(self) -> Dict[Any, List]:
        """Infer groups from internal `data` columns

        :return: found groups
        """
        groups: Dict[Any, List] = {}
        for index in self.data.columns:
            cat, a = self.from_index(index)
            if cat not in groups:
                groups[cat] = []
            groups[cat].append(a)
        return groups

    def submatrix(self, row_group: Any, col_group: Any) -> Matrix:
        """Return the subpart of matrix with given groups.

        :param row_group: group for rows
        :param col_group: group for columns
        :return:
            matrix containing the groups vertices, with the groups labels
            removed
        """
        row = [(row_group, k) for k in self.row_groups[row_group]]
        col = [(col_group, k) for k in self.column_groups[col_group]]
        return Matrix(
            DataFrame(
                self.data.loc[row, col].values,
                index=self.row_groups[row_group],
                columns=self.column_groups[col_group],
            )
        )

    def subblock(self, row_group: Any, col_group: Any) -> BlockMatrix:
        """Return the sub block of matrix with given groups.

        :param row_group: group for rows
        :param col_group: group for columns
        :return:
            block matrix containing the groups vertices,
        """
        row = [(row_group, k) for k in self.row_groups[row_group]]
        col = [(col_group, k) for k in self.column_groups[col_group]]
        return BlockMatrix(
            DataFrame(
                self.data.loc[row, col].values,
                index=row,
                columns=col,
            )
        )


class SparseAdjacencyMatrix(Matrix):
    """This class implements graphs as a generic adjacency matrix.

    The adjacency matrix is represented internally by a
    :class:`pandas.DataFrame` with vertices as the indexes and columns.
    Vertices on rows and columns may differ.

    :param data: adjacency matrix in an array-like or dict-structure

    .. note:: the cells of the matrix can be of any type (not just numerics)
    """

    @property
    def vertices(self) -> List:
        """Return list of vertices"""
        return list(
            set(self.data.index.tolist()).union(
                set(self.data.columns.tolist())
            )
        )

    def plot(
        self,
        edge_label: bool = False,
        self_loop: bool = False,
        cut: float | Callable[[Any], bool] = -float("inf"),
    ) -> Digraph:
        """Create a graph for adjacency matrix.

        This function creates a Graph using graphviz and display it.

        :param edge_label: (optional) parameter to display the value of edges
        :param self_loop: (optional) parameter to display self looping edges
        :param cut:
            either a numeric threshold under which edges are pruned, or a
            filtering function taking one cell and returning if edge must be
            pruned (boolean)
        """
        graph = Digraph("graph", strict=True)
        graph.attr("node", shape="box")

        for v in self.vertices:
            graph.node(str(v))
        for a in self.data.index:
            for b in self.data.columns:
                if not self_loop and a == b:
                    continue
                if isinstance(cut, float) and self.data.at[a, b] < cut:
                    continue
                elif callable(cut) and cut(self.data.at[a, b]):
                    continue
                graph.edge(
                    str(a),
                    str(b),
                    label=str(self.data.at[a, b]) if edge_label else "",
                )
        graph.render()
        return graph


class SparseBlockAdjacencyMatrix(BlockMatrix, SparseAdjacencyMatrix):
    """This class implements graphs as a block adjacency matrix.

    The adjacency matrix is represented internally by a
    :class:`pandas.DataFrame` with vertices as the indexes and columns.
    Vertices on rows and columns may differ.

    Index and column names are all parts of a group, and are formatted as such:
    (`group_label`, `vertex_label`)

    :param data: adjacency matrix in an array-like or dict-structure
    :raise TypeError: if any index or column name is not properly formatted

    .. note:: the cells of the matrix can be of any type (not just numerics)

    .. warning::
        For future compatibility, do not manipulate the indexes directly and
        use :meth:`to_index` and :meth:`from_index` instead.
    """

    def subblock(
        self, row_group: Any, col_group: Any
    ) -> SparseBlockAdjacencyMatrix:
        """Return the sub block of matrix with given groups.

        :param row_group: group for rows
        :param col_group: group for columns
        :return:
            block matrix containing the groups vertices,
        """
        row = [(row_group, k) for k in self.row_groups[row_group]]
        col = [(col_group, k) for k in self.column_groups[col_group]]
        return SparseBlockAdjacencyMatrix(
            DataFrame(
                self.data.loc[row, col].values,
                index=row,
                columns=col,
            )
        )


class AdjacencyMatrix(SparseAdjacencyMatrix):
    """This class implements graphs as an adjacency matrix.

    The adjacency matrix is represented internally by a
    :class:`pandas.DataFrame` with vertices as the indexes and columns.

    :param data: adjacency matrix in an array-like or dict-structure
    :param vertices:

    :raise ValueError: if columns and rows have different sets of labels

    .. note:: the cells of the matrix can be of any type (not just numerics)
    """

    def __init__(self, data, vertices: List = None):
        df = DataFrame(
            data.values if isinstance(data, DataFrame) and vertices else data,
            index=vertices,
            columns=vertices,
        )
        if df.columns.tolist() != df.index.tolist():
            raise ValueError(
                f"{self.__class__} supports only same labelled"
                "index and columns"
            )

        super().__init__(df)

    @property
    def vertices(self) -> List:
        """Return list of vertices"""
        return self.data.index.tolist()

    def plot(
        self,
        edge_label: bool = False,
        self_loop: bool = False,
        cut: float | Callable[[Any], bool] = -float("inf"),
    ) -> Digraph:
        """Create a graph for adjacency matrix.

        This function creates a Graph using graphviz and display it.

        :param edge_label: (optional) parameter to display the value of edges
        :param self_loop: (optional) parameter to display self looping edges
        :param cut:
            either a numeric threshold under which edges are pruned, or a
            filtering function taking one cell and returning if edge must be
            pruned (boolean)
        """
        graph = Digraph("graph", strict=True)
        graph.attr("node", shape="box")

        for v in self.vertices:
            graph.node(str(v))
        for a in self.vertices:
            for b in self.vertices:
                if not self_loop and a == b:
                    continue
                if isinstance(cut, float) and self.data.at[a, b] < cut:
                    continue
                elif callable(cut) and cut(self.data.at[a, b]):
                    continue
                if self.data.at[a, b] != 0:
                    graph.edge(
                        str(a),
                        str(b),
                        label=str(self.data.at[a, b]) if edge_label else "",
                    )
        graph.render()
        return graph


class BlockAdjacencyMatrix(AdjacencyMatrix, SparseBlockAdjacencyMatrix):
    """This class represents adjacency matrices with 2-dimensional vertices.

    The block matrix is represented internally by a
    :class:`pandas.DataFrame` with vertices as the indexes and columns.

    Vertices are all parts of a group, and are formatted as such:
    (`group_label`, `vertex_label`)

    :param data: adjacency matrix in an array-like or dict-structure
    :param groups: groups of vertices, overrides `data` vertices

    :raise ValueError: if columns and rows have different sets of labels
    :raise TypeError: if any index or column name is not properly formatted

    .. warning::
        For future compatibility, do not manipulate the indexes directly and
        use :meth:`to_index` and :meth:`from_index` instead.
    """

    def __init__(self, data, groups: Dict[Any, List] = None):
        vertices = (
            None
            if groups is None
            else [
                self.to_index(c, v)
                for c, values in groups.items()
                for v in values
            ]
        )
        super().__init__(data, vertices=vertices)

    @property
    def groups(self) -> Dict[Any, List]:
        """Return dictionary of groups."""
        return self.row_groups


class ProfileAlternativeMatrix(BlockAdjacencyMatrix):
    """This class represents adjacency matrices with both profiles and
    alternatives.

    It is a constrained case of :class:`BlockMatrix` that must contain
    a group of alternatives and a group of profiles, and no other group.

    The block matrix is represented internally by a
    :class:`pandas.DataFrame` with vertices as the indexes and columns.

    :param data: adjacency matrix in an array-like or dict-structure
    :param alternatives:
    :param profiles:

    :raise ValueError: if columns and rows have different sets of labels
    :raise ValueError:
        if the inferred groups is not the pair (alternatives, profiles)

    .. warning::
        For future compatibility, do not manipulate the indexes directly and
        use :meth:`alternative_index` and :meth:`profile_index` instead.
    """

    ALTERNATIVES = "alternatives"
    PROFILES = "profiles"
    ALLOWED_GROUPS = {ALTERNATIVES, PROFILES}

    def __init__(self, data, alternatives: List = None, profiles: List = None):
        if profiles and alternatives:
            groups = {
                self.ALTERNATIVES: alternatives,
                self.PROFILES: profiles,
            }
        else:
            groups = None
        super().__init__(data, groups)
        if set(self.groups.keys()) != self.ALLOWED_GROUPS:
            raise ValueError(
                "This class only works with two groups: "
                f"{self.ALLOWED_GROUPS}"
            )

    @classmethod
    def alternative_index(cls, alternative: Any) -> Any:
        """Format an alternative index.

        :param alternative:
        :return: formatted index
        """
        return cls.to_index(cls.ALTERNATIVES, alternative)

    @classmethod
    def profile_index(cls, profile: Any) -> Any:
        """Format a profile index.

        :param profile:
        :return: formatted index
        """
        return cls.to_index(cls.PROFILES, profile)

    @property
    def alternatives(self) -> List:
        """Return list of alternatives"""
        return self.groups[self.ALTERNATIVES]

    @property
    def profiles(self) -> List:
        """Return list of profiles"""
        return self.groups[self.PROFILES]


class BinaryAdjacencyMatrix(AdjacencyMatrix):
    """This class implements graphs as a binary adjacency matrix.

    The adjacency matrix is represented internally by a
    :class:`pandas.DataFrame` with vertices as the indexes and columns.

    :param data: adjacency matrix in an array-like or dict-structure
    :param vertices:

    :raise ValueError: if non-binary values are in the matrix
    :raise ValueError: if columns and rows have different sets of labels
    """

    def __init__(self, data, vertices: List = None):
        super().__init__(data, vertices)
        if ((self.data != 1) & (self.data != 0)).any(axis=None):
            raise ValueError(
                "AdjacencyMatrix objects must contain binary values"
            )

    @property
    def transitive_closure(self) -> "BinaryAdjacencyMatrix":
        """Return transitive closure of matrix"""
        _m = floyd_warshall(csr_matrix(self.data.to_numpy())) < float("inf")
        m = DataFrame(
            _m,
            index=self.vertices,
            columns=self.vertices,
        )
        res = DataFrame(
            0,
            index=self.vertices,
            columns=self.vertices,
        )
        res[m] = 1
        return self.__class__(res)

    @property
    def transitive_reduction(self) -> "BinaryAdjacencyMatrix":
        """Return transitive reduction of matrix.

        .. note:: this function can change the matrix shape
        """
        matrix = self.graph_condensation
        path_matrix = floyd_warshall(csr_matrix(matrix.data.to_numpy())) == 1
        nodes = range(len(matrix.data))
        for u in nodes:
            for v in nodes:
                if path_matrix[u][v]:
                    for w in nodes:
                        if path_matrix[v][w]:
                            matrix.data.iloc[u, w] = 0
        return matrix

    @property
    def graph_condensation(self) -> "BinaryAdjacencyMatrix":
        """Return the condensation graph

        .. note:: the matrix output by this function is acyclic

        .. warning:: this function changes the matrix shape
        """

        n_components, labels = connected_components(
            self.data.to_numpy(), connection="strong"
        )
        # Return input matrix if no cycle found
        if n_components == len(self.data):
            return self.__class__(self.data)
        # Create new matrix with appropriate names for components
        components = []
        for component_index in range(n_components):
            component = HashableSet(
                self.data.index[labels == component_index].tolist()
            )
            components.append(component)
        new_matrix = DataFrame(0, index=components, columns=components)
        for component_a, component_b in product(
            range(n_components), range(n_components)
        ):
            if component_a != component_b:
                new_matrix.iloc[component_a, component_b] = (
                    self.data.iloc[
                        labels == component_a, labels == component_b
                    ]
                    .to_numpy()
                    .any()
                )

        return self.__class__(new_matrix.astype(int))

    @property
    def cycle_reduction_matrix(self) -> "BinaryAdjacencyMatrix":
        """Return matrix with cycles removed."""
        n_components, labels = connected_components(
            self.data.to_numpy(), connection="strong"
        )
        components = range(n_components)
        new_matrix = DataFrame(0, index=self.vertices, columns=self.vertices)
        for component_a, component_b in product(components, components):
            if component_a != component_b:
                new_matrix.loc[
                    labels == component_a, labels == component_b
                ] = (
                    self.data.loc[labels == component_a, labels == component_b]
                    .to_numpy()
                    .any()
                )
        return self.__class__(new_matrix.astype(int))

    @property
    def kernel(self) -> List:
        """Return the kernel of the graph if existing.

        The kernel is a *stable* and *dominant* set of nodes.
        Dominant nodes are the origin of edges, dominated ones are the target.

        :return: the kernel (if existing), else an empty list
        """
        graph = self.data.copy()
        # We remove self loops
        for v in self.vertices:
            graph.at[v, v] = 0
        kernel: Set = set()
        outsiders: Set = set()
        while not graph.empty:
            domination = (graph == 0).all(axis=0)
            dominators = domination[domination].index.tolist()
            if len(dominators) == 0:
                return []

            dominated = (graph == 1).loc[dominators].any(axis=0)
            neighbours = dominated[dominated].index.tolist()

            to_remove = dominators + neighbours
            graph = graph.drop(index=to_remove, columns=to_remove)
            kernel = kernel.union(dominators)
            outsiders = outsiders.union(neighbours)
        return list(kernel)
