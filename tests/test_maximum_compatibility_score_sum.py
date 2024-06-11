from typing import List

import pytest

from src import maximum_compatibility_score_sum


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "students, mentors, expected",
    [
        ([[1, 1, 0], [1, 0, 1], [0, 0, 1]], [[1, 0, 0], [0, 0, 1], [1, 1, 0]], 8),
        ([[0, 0], [0, 0], [0, 0]], [[1, 1], [1, 1], [1, 1]], 0),
    ],
)
def test_maximum_compatibility_score_sum(
    students: List[List[int]], mentors: List[List[int]], expected: int
) -> None:
    assert maximum_compatibility_score_sum(students, mentors) == expected
