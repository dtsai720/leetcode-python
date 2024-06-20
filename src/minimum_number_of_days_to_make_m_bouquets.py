from typing import List


def minimum_number_of_days_to_make_m_bouquets(
    bloom_day: List[int], m: int, k: int
) -> int:
    """
    Given an integer array bloom_day, an integer m, and an integer k. We need to make m bouquets.
    To make a bouquet, you need to use k adjacent flowers from the garden.
    The garden consists of n flowers, the ith flower will bloom in the bloom_day[i] and
    then can be used in exactly one bouquet. Return the minimum number of days you need to wait
    to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

    Args:
        bloom_day (List[int]): List of integers where bloom_day[i] is the day the ith flower
        will bloom.
        m (int): Number of bouquets to make.
        k (int): Number of adjacent flowers to make a bouquet.

    Returns:
        int: The minimum number of days you need to wait to be able to make m bouquets from
        the garden.
    """

    if not (
        isinstance(bloom_day, list)
        and all(isinstance(i, int) for i in bloom_day)
        and isinstance(m, int)
        and isinstance(k, int)
    ):
        raise TypeError(
            "blooms_day must be a list of integers, m and k must be integers."
        )

    def is_possible(days: int) -> bool:
        count = 0
        output = 0
        for num in bloom_day:
            if num <= days:
                count += 1
                if count == k:
                    output += 1
                    count = 0
            else:
                count = 0
        return output >= m

    output = -1
    start, end = min(bloom_day), max(bloom_day)
    while start <= end:
        mid = start + (end - start) // 2
        if is_possible(mid):
            output = mid
            end = mid - 1
        else:
            start = mid + 1

    return output
