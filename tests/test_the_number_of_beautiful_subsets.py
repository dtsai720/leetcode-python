from typing import List

import pytest

from src import the_number_of_beautiful_subsets


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "nums, k, expected",
    [([2, 4, 6], 2, 4), ([1], 1, 1)],
)
def test_the_number_of_beautiful_subsets(nums: List[int], k: int, expected: int):
    assert the_number_of_beautiful_subsets(nums, k) == expected
