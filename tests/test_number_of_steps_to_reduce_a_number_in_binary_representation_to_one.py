import pytest

from src import number_of_steps_to_reduce_a_number_in_binary_representation_to_one


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "s, expected",
    [
        ("1101", 6),
        ("10", 1),
        ("1", 0),
    ],
)
def test_number_of_steps_to_reduce_a_number_in_binary_representation_to_one(
    s: str, expected: int
):
    assert (
        number_of_steps_to_reduce_a_number_in_binary_representation_to_one(s)
        == expected
    )
