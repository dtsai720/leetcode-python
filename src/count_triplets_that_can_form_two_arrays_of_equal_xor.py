from collections import defaultdict
from typing import List


def count_triplets_that_can_form_two_arrays_of_equal_xor(nums: List[int]) -> int:
    """
    Function docstring: This function counts the number of triplets (i, j, k)
    where 0 <= i < j <= k < nums.length
    such that the XOR of all the elements of nums between i and j-1,
    and the XOR of all the elements of nums between j and k, are equal.

    Args:
        nums: List[int] : List of integers

    Returns:
        int : Number of triplets
    """
    if not (isinstance(nums, list) and all(isinstance(num, int) for num in nums)):
        raise TypeError("nums must be a non-empty list of integers")

    cnt, total = defaultdict(int), defaultdict(int)
    cnt[0] = 1
    output, current = 0, 0
    for idx, num in enumerate(nums):
        current ^= num
        if current in cnt:
            output += cnt[current] * idx - total[current]
        cnt[current] += 1
        total[current] += idx + 1

    return output
