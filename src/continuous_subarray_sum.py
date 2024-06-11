from typing import List


def continuous_subarray_sum(nums: List[int], k: int) -> bool:
    """
    Given a list of non-negative numbers and a target integer k,
    write a function to check if the array has a continuous subarray of size
    at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

    Args:
        nums : List[int] : list of non-negative numbers
        k : int : target integer

    Returns:
        bool : True if the array has a continuous subarray of size
        at least 2 that sums up to a multiple of k, False otherwise
    """
    if not (
        isinstance(nums, list)
        and all(isinstance(num, int) for num in nums)
        and isinstance(k, int)
    ):
        raise TypeError("nums should be a list of integers and k should be an integer")

    prefix_sum = 0
    seen = set()

    for num in nums:
        prefix_sum = (prefix_sum + num) % k
        if prefix_sum in seen:
            return True
        seen.add((((prefix_sum - num) % k) + k) % k)

    return False
