from bisect import bisect_left

from typing import List


def special_array_with_x_elements_greater_than_or_equal_x(nums: List[int]) -> int:
    """
    Given an array of integers nums, a move consists of choosing any element
    and decreasing it by 1.
    An array A is special if for every integer x
    (x is the number of moves needed to decrease an element to 0 or less),
    there are at least x elements in A that are greater than or equal to x.
    Return the minimum number of moves needed to make array A special.

    Args:
        nums: List[int] : List of integers

    Returns:
        int : Minimum number of moves needed to make array A special
    """
    if not (isinstance(nums, list) and all(isinstance(num, int) for num in nums)):
        raise TypeError("nums must be a non-empty list of integers")

    if not nums:
        return -1

    nums.sort()
    min_value, max_value = 0, nums[-1]
    while min_value <= max_value:
        mid_value = (min_value + max_value) // 2
        idx = bisect_left(nums, mid_value)
        if len(nums) - idx == mid_value:
            return mid_value
        if len(nums) - idx < mid_value:
            max_value = mid_value - 1
        else:
            min_value = mid_value + 1
    return -1
