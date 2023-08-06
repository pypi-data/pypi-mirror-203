from __future__ import annotations

from typing import Any, Dict, List, Union, cast

from pandas import DataFrame, Series
from pandas.api.types import is_numeric_dtype  # type: ignore

import mcda.core.criteria_functions

from .aliases import Function
from .matrices import Matrix
from .scales import QuantitativeScale, Scale
from .values import Container, ScaleValues


class PerformanceTable(Matrix):
    """This class is used to represent performance tables.

    :param data: performance table in an array-like or dict structure
    :param scales: criteria scales (scales are inferred from data if not set)
    :param alternatives:
    :param criteria:

    :attr df: dataframe containing the performances
    :attr scales: criteria scales

    .. note::
        when applying pandas methods to modify the performance table, do it
        this way: `table.df = table.df.method()` (for a method called `method`)

        Also you may want to modify the criteria scales depending on such
        modifications.
    """

    def __init__(
        self,
        data,
        scales: Dict[Any, Scale] = None,
        alternatives: List[Any] = None,
        criteria: List[Any] = None,
    ):
        df = DataFrame(data, index=alternatives, columns=criteria)
        super().__init__(df)
        self.scales = self.bounds if scales is None else scales

    def __eq__(self, other) -> bool:
        """Check equality of performance tables.

        Equality is defines as having the same set of scales, and having the
        same dataframe.

        :return: ``True`` if both are equal
        """
        if not isinstance(other, PerformanceTable):
            return False
        _table = cast(PerformanceTable, other)
        if self.scales == _table.scales:
            return super().__eq__(_table)
        return False

    @property
    def criteria(self) -> List[Any]:
        """Return performance table criteria"""
        return self.data.columns.tolist()

    @property
    def alternatives(self) -> List[Any]:
        """Return performance table alternatives"""
        return self.data.index.tolist()

    @property
    def alternatives_values(self) -> Container[ScaleValues]:
        """Iterator on the table alternatives values"""
        return Container[ScaleValues](
            dict(
                (a, ScaleValues(self.data.loc[a], self.scales))
                for a in self.alternatives
            )
        )

    @property
    def criteria_values(self) -> Container[ScaleValues]:
        """Iterator on the table criteria values"""
        return Container[ScaleValues](
            dict(
                (c, ScaleValues(self.data[c], self.scales[c]))
                for c in self.criteria
            )
        )

    @property
    def is_numeric(self) -> bool:
        """Check whether performance table is numeric.

        :return:
        :rtype: bool
        """
        for col in self.data.columns:
            if not is_numeric_dtype(self.data[col]):
                return False
        return True

    @property
    def bounds(self) -> Dict[Any, Scale]:
        """Return criteria scales inferred from performance table values.

        .. note::
            will always assume maximizable quantitative scales for numeric
            criteria and nominal scales for others
        """
        return {
            criterion: ScaleValues(self.data[criterion]).bounds
            for criterion in self.criteria
        }

    @property
    def efficients(self) -> List:
        """Return efficient alternatives.

        This is the list of alternatives that are not strongly dominated by
        another one.

        :return:
        """
        res = set(self.alternatives)
        for avalues in self.alternatives_values:
            dominated = set()
            for b in res:
                if avalues.name == b:
                    continue
                if avalues.dominate_strongly(self.alternatives_values[b]):
                    dominated.add(b)
            res -= dominated
        return sorted(res, key=lambda a: self.alternatives.index(a))

    def _apply_criteria_functions(
        self, functions: Dict[Any, Function]
    ) -> "PerformanceTable":
        """Apply criteria functions to performance table and return result.

        :param functions: functions identified by their criterion
        :return:
        """
        return PerformanceTable(
            self.data.apply(
                lambda col: col.apply(functions.get(col.name, lambda x: x))
            ),
            self.scales,
        )

    def apply(
        self, functions: mcda.core.criteria_functions.CriteriaFunctions
    ) -> "PerformanceTable":
        """Apply criteria functions to performance table and return result.

        :param functions:
        :return:
        """
        return functions(self)

    @property
    def within_criteria_scales(self) -> "PerformanceTable":
        """Return a table indicating which performances are within their
        respective criterion scale.

        :return:
        """
        return self._apply_criteria_functions(
            {
                criterion: cast(
                    Function, lambda x, c=criterion: x in self.scales[c]
                )
                for criterion in self.scales.keys()
            },
        )

    @property
    def is_within_criteria_scales(self) -> bool:
        """Check whether all cells are within their respective criteria scales.

        :return:
        """
        return self.within_criteria_scales.data.all(None)

    def transform(
        self,
        out_scales: Dict[Any, Scale],
    ) -> "PerformanceTable":
        """Transform performances table between scales.

        :param out_scales: target criteria scales
        :return: transformed performance table
        """
        functions = {
            criterion: (
                cast(
                    Function,
                    lambda x, c=criterion: self.scales[c].transform(
                        x, out_scales[c]
                    ),
                )
            )  # https://bugs.python.org/issue13652
            for criterion in self.scales.keys()
        }
        return PerformanceTable(
            self._apply_criteria_functions(functions).data, out_scales
        )

    def normalize_without_scales(self) -> "PerformanceTable":
        """Normalize performance table using criteria values bounds.

        :return:
        :raise TypeError: if performance table is not numeric
        """
        return PerformanceTable(self.data).normalize()

    def normalize(self) -> "PerformanceTable":
        """Normalize performance table using criteria scales.

        :return:
        """
        return self.transform(
            {
                criterion: QuantitativeScale.normal()
                for criterion in self.criteria
            }
        )

    def sum(self, axis: int = None) -> Union[Series, float]:
        """Sum performances.

        Behaviour depends on `axis` value:

        * ``0``: returns column sums as a list
        * ``1``: returns row sums as a list
        * else: returns sum on both dimension as a numeric value

        :param axis: axis on which the sum is made
        :return:

        .. note::
            Non-numeric values are simply ignored as well as non-numeric sums
        """
        if axis is not None:
            return self.data.sum(axis=axis, numeric_only=True)
        return self.data.sum(numeric_only=True).sum()

    def subtable(
        self, alternatives: List[Any] = None, criteria: List[Any] = None
    ) -> "PerformanceTable":
        """Return the subtable containing given alternatives and criteria.

        :param alternatives:
        :param criteria:
        :return:
        """
        alternatives = (
            self.alternatives if alternatives is None else alternatives
        )
        criteria = self.criteria if criteria is None else criteria
        return self.__class__(
            self.data.loc[alternatives, criteria],
            {criterion: self.scales[criterion] for criterion in criteria},
        )
