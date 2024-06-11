def get_equal_substrings_within_budget(s: str, t: str, max_cost: int) -> int:
    """
    Find the maximum length of a substring that can be made equal by changing characters
    within a given budget.

    Args:
        s (str): The first string.
        t (str): The second string.
        max_cost (int): The maximum cost of changing characters.

    Returns:
        int: The maximum length of a substring that can be made equal.
    """
    if (
        not isinstance(s, str)
        or not isinstance(t, str)
        or not isinstance(max_cost, int)
    ):
        raise TypeError("s and t should be strings and max_cost should be an integer")

    if len(s) != len(t):
        raise ValueError("s and t should be of the same length")

    max_length = 0
    slow = -1
    for fast, char in enumerate(s):
        max_cost -= abs(ord(char) - ord(t[fast]))
        while max_cost < 0:
            slow += 1
            max_cost += abs(ord(s[slow]) - ord(t[slow]))
        max_length = max(max_length, fast - slow)

    return max_length
