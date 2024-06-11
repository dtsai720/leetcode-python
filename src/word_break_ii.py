from typing import List, Set


def word_break_ii(s: str, candidates: List[str]) -> List[str]:
    """
    This function performs a word break operation.
    It takes a string 's' and a list of candidate words 'candidates',
    and returns a list of strings where each string is a possible sentence
    formed by concatenating words from 'candidates' that can form 's'.

    Args:
        s: str : Input string
        candidates: List[str] : List of candidate words

    Returns:
        List[str] : List of strings where each string is a possible sentence
        formed by concatenating words from 'candidates' that can form 's'
    """
    if not (
        isinstance(s, str)
        and isinstance(candidates, list)
        and all(isinstance(word, str) for word in candidates)
    ):
        raise ValueError("s must be a string and candidates must be a list of strings")

    words: Set[str] = set()
    sizes: Set[int] = set()

    for word in candidates:
        words.add(word)
        sizes.add(len(word))

    output: List[str] = []

    def __helper(idx: int, array: List[str]):
        if idx == len(s):
            output.append(" ".join(array))
            return

        for size in sizes:
            if idx + size > len(s):
                continue

            word = s[idx : idx + size]
            if word in words:
                array.append(word)
                __helper(idx + size, array)
                array.pop()

    __helper(0, [])

    return output
