from typing import List

import pytest

from src import hand_of_straights


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True),
        ([1, 2, 3, 4, 5], 4, False),
    ],
)
def test_hand_of_straights(nums: List[int], k: int, expected: bool):
    result = hand_of_straights(nums, k)
    assert result is expected
