from typing import List

import pytest

from src import word_break_ii


# pylint: disable=missing-function-docstring
@pytest.mark.parametrize(
    "s, words, expected",
    [
        (
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"],
            ["cat sand dog", "cats and dog"],
        ),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"],
        ),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
    ],
)
def test_word_break_iii(s: str, words: List[str], expected: List[str]):
    assert sorted(word_break_ii(s, words)) == sorted(expected)
