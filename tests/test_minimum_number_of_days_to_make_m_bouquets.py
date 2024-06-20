from typing import List

import pytest

from src import minimum_number_of_days_to_make_m_bouquets


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "bloom_day, m, k, expected",
    [
        ([1, 10, 3, 10, 2], 3, 1, 3),
        ([1, 10, 3, 10, 2], 3, 2, -1),
        ([7, 7, 7, 7, 12, 7, 7], 2, 3, 12),
    ],
)
def test_minimum_number_of_days_to_make_m_bouquets(
    bloom_day: List[int], m: int, k: int, expected: int
):
    assert minimum_number_of_days_to_make_m_bouquets(bloom_day, m, k) == expected
