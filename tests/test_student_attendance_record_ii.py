import pytest

from src import student_attendance_record_ii


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "n, expected",
    [(2, 8), (1, 3), (10101, 183236316)],
)
def test_student_attendance_record(n: int, expected: int):
    assert student_attendance_record_ii(n) == expected
