from collections import Counter
from typing import List


def hand_of_straights(nums: List[int], k: int) -> bool:
    """
    Given an array of integers nums and an integer k,
    return true if it is possible to divide this array into k non-empty subsets
    whose sums are all equal.

    Args:
        nums: List[int] : List of integers
        k: int : Integer

    Returns:
        bool : True if it is possible to divide this array into k non-empty subsets
        whose sums are all equal, False otherwise
    """
    if not (isinstance(nums, list) and all(isinstance(num, int) for num in nums)):
        raise TypeError("nums must be a non-empty list of integers")

    if len(nums) % k != 0:
        return False

    nums.sort()
    count = Counter(nums)
    for num in nums:
        if count[num] == 0:
            continue
        for i in range(k):
            if count[num + i] == 0:
                return False
            count[num + i] -= 1
    return True
