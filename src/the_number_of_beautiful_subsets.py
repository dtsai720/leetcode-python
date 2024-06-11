from typing import List


from src.common import binary_search


def the_number_of_beautiful_subsets(nums: List[int], k: int) -> int:
    """
    Calculate the number of beautiful subsets in the given list of integers.

    Args:
        nums (List[int]): A list of integers.
        k (int): An integer.

    Returns:
        int: The number of beautiful subsets in the given list of integers.
    """
    if not (
        isinstance(nums, list)
        and isinstance(k, int)
        and all(isinstance(num, int) for num in nums)
    ):
        raise TypeError(
            "nums must be a non-empty list of integers and k must be an integer"
        )

    nums.sort()

    def __helper(array: List[int], idx: int) -> int:
        if idx == len(nums):
            return 0

        count = __helper(array, idx + 1)
        if binary_search(array, nums[idx] - k) == -1:
            array.append(nums[idx])
            count += 1 + __helper(array, idx + 1)
            array.pop()
        return count

    return __helper([], 0)
