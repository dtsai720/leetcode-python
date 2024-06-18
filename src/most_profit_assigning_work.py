from typing import List
import heapq


def max_profit_assignment(
    difficulty: List[int], profit: List[int], worker: List[int]
) -> int:
    """
    Given two lists of integers difficulty and profit,
    where profit[i] is the profit of completing the ith job,
    and difficulty[i] is the difficulty of the ith job.

    Now, we have a list of workers. Each worker is assigned a job in the list of jobs.

    A worker's profit is the sum of profit of each job assigned to him.
    A worker can be assigned at most one job.

    Return the maximum profit the workers can make.

    Args:
        difficulty: a list of integers representing the difficulty of each job
        profit: a list of integers representing the profit of each job
        worker: a list of integers representing the workers

    Returns:
        int: the maximum profit the workers can make
    """
    if not (
        isinstance(difficulty, list)
        and isinstance(profit, list)
        and isinstance(worker, list)
        and all(isinstance(x, int) for x in difficulty)
        and all(isinstance(x, int) for x in profit)
        and all(isinstance(x, int) for x in worker)
    ):
        raise TypeError("difficulty, profit, and worker must be a list of integers")

    nums = []
    heapq.heapify(nums)

    for a, b in zip(difficulty, profit):
        heapq.heappush(nums, (-b, a))

    output = 0
    for w in sorted(worker, reverse=True):
        while nums and w < nums[0][1]:
            heapq.heappop(nums)
        if not nums:
            return output
        output += -nums[0][0]
    return output
