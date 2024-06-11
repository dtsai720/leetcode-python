from typing import List

import pytest

from src import replace_words


@pytest.mark.parametrize(
    "dictionary, sentence, expected",
    [
        (
            ["cat", "bat", "rat"],
            "the cattle was rattled by the battery",
            "the cat was rat by the bat",
        ),
        (
            ["a", "aa", "aaa", "aaaa"],
            "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa",
            "a a a a a a a a bbb baba a",
        ),
    ],
)
def test_replace_words(dictionary: List[str], sentence: str, expected: str):
    """
    Test the replace_words function with various inputs and expected outputs.

    Args:
        dictionary (List[str]): A list of words.
        sentence (str): A sentence with all words separated by space.
        expected (str): A sentence with all words replaced by the root word.
    """
    assert replace_words(dictionary, sentence) == expected
