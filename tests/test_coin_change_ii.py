from typing import List

import pytest

from src import coin_change_ii


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        ([1, 2, 5], 5, 4),
        ([2], 3, 0),
        ([10], 10, 1),
    ],
)
def test_coin_change_ii(coins: List[int], amount: int, expected: int):
    assert coin_change_ii(coins, amount) == expected
