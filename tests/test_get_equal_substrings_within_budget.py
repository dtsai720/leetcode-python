import pytest

from src import get_equal_substrings_within_budget


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "s, t, max_cost, expected",
    [
        ("abcd", "bcdf", 3, 3),
        ("abcd", "cdef", 3, 1),
        ("abcd", "acde", 0, 1),
    ],
)
def test_get_equal_substrings_within_budget(
    s: str, t: str, max_cost: int, expected: int
):
    assert get_equal_substrings_within_budget(s, t, max_cost) == expected
