from typing import List

import pytest

from src import continuous_subarray_sum


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([23, 2, 4, 6, 7], 6, True),
        ([23, 2, 6, 4, 7], 6, True),
        ([23, 2, 6, 4, 7], 13, False),
    ],
)
def test_continuous_subarray_sum(nums: List[int], k: int, expected: bool):
    assert continuous_subarray_sum(nums, k) is expected
