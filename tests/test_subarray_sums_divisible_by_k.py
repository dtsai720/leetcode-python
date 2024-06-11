from typing import List

import pytest

from src import subarray_sums_divisible_by_k


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([4, 5, 0, -2, -3, 1], 5, 7),
        ([5], 9, 0),
    ],
)
def test_subarray_sums_divisible_by_k(nums: List[int], k: int, expected: int):
    assert subarray_sums_divisible_by_k(nums, k) == expected
