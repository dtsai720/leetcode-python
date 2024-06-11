from typing import List

import pytest

from src import special_array_with_x_elements_greater_than_or_equal_x


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "nums, expected",
    [([3, 5], 2), ([0, 0], -1), ([0, 4, 3, 0, 4], 3)],
)
def test_special_array_with_x_elements_greater_than_or_equal_x(
    nums: List[int], expected: int
):
    assert special_array_with_x_elements_greater_than_or_equal_x(nums) == expected
