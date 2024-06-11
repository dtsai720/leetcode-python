from typing import List

import pytest

from src import count_triplets_that_can_form_two_arrays_of_equal_xor


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 6, 7], 4),
        ([1, 1, 1, 1, 1], 10),
    ],
)
def test_count_triplets_that_can_form_two_arrays_of_equal_xor(
    nums: List[int], expected: int
):
    assert count_triplets_that_can_form_two_arrays_of_equal_xor(nums) == expected
