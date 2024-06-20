from typing import List

import pytest

from src import magnetic_force_between_two_balls


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "position, m, expected",
    [
        ([1, 2, 3, 4, 7], 3, 3),
        ([5, 4, 3, 2, 1, 1000000000], 2, 999999999),
    ],
)
def test_magnetic_force_between_two_balls(position: List[int], m: int, expected: int):
    assert magnetic_force_between_two_balls(position, m) == expected
