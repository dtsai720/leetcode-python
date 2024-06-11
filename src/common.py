from typing import List


def binary_search(array: List[int], num: int) -> int:
    """
    Perform a binary search on a sorted list.

    Args:
        array (List[int]): A sorted list of integers.
        num (int): An integer to search for in the list.

    Returns:
        int: The index of the integer in the list if found, otherwise -1.
    """
    if not (
        isinstance(array, list)
        and isinstance(num, int)
        and all(isinstance(x, int) for x in array)
    ):
        raise TypeError(
            "array should be a list of integers and num should be an integer"
        )

    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == num:
            return mid
        if array[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1
