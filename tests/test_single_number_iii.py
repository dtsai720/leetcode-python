from typing import List

import pytest

from src import single_number_iii


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 1, 3, 2, 5], [3, 5]),
        ([-1, 0], [-1, 0]),
        ([0, 1], [0, 1]),
    ],
)
def test_single_number_iii(nums: List[int], expected: List[int]):
    assert sorted(single_number_iii(nums)) == expected
