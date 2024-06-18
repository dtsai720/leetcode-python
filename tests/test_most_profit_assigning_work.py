from typing import List

import pytest

from src import max_profit_assignment


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "difficulty, profit, worker, expected",
    [
        ([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7], 100),
        ([85, 47, 57], [24, 66, 99], [40, 25, 25], 0),
    ],
)
def test_max_profit_assignment(
    difficulty: List[int], profit: List[int], worker: List[int], expected: int
):
    assert max_profit_assignment(difficulty, profit, worker) == expected
