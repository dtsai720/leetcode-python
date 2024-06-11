from typing import List


def subarray_sums_divisible_by_k(nums: List[int], k: int) -> int:
    """
    Given an array A of integers, return the number of (contiguous, non-empty) subarrays
    that have a sum divisible by K.

    Args:
        nums: List[int] : List of integers
        k: int : Integer

    Returns:
        int : Number of contiguous subarrays that have a sum divisible by K
    """
    if not (
        isinstance(nums, list)
        and all(isinstance(num, int) for num in nums)
        and isinstance(k, int)
    ):
        raise TypeError(
            "nums must be a non-empty list of integers and k must be an integer"
        )

    count = [0] * k
    count[0] = 1
    prefix_sum, output = 0, 0
    for num in nums:
        prefix_sum = (prefix_sum + num) % k
        output += count[prefix_sum]
        count[prefix_sum] += 1
    return output
