from typing import List


def single_number_iii(nums: List[int]) -> List[int]:
    """
    Function docstring: This function takes a list of integers and
    returns a list of integers that appear only once in the input list.

    Args:
        nums: List[int] : List of integers

    Returns:
        List[int] : List of integers that appear only once in the input list
    """
    if not (isinstance(nums, list) and all(isinstance(num, int) for num in nums)):
        raise TypeError("nums must be a non-empty list of integers")

    myset = set()
    for num in nums:
        if num in myset:
            myset.remove(num)
        else:
            myset.add(num)
    return list(myset)
