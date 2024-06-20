from typing import List


def magnetic_force_between_two_balls(position: List[int], m: int) -> int:
    """
    Given an integer array position where position[i] is the position of the ith ball in the row,
    and an integer m representing the number of balls in the row.
    Return the minimum force required to move all the balls to the same position
    (i.e., the minimum maximum force to move all the balls).

    Args:
        position (List[int]): List of integers where position[i] is the position of the ith ball
        in the row.
        m (int): Number of balls in the row.

    Returns:
        int: The minimum force required to move all the balls to the same position.
    """
    if not (
        isinstance(position, list)
        and all(isinstance(i, int) for i in position)
        and isinstance(m, int)
    ):
        raise TypeError("position must be a list of integers and m must be an integer.")

    def is_possible(distance: int) -> bool:
        prev_position = position[0]
        balls_count = 1

        for idx in range(1, len(position)):
            if position[idx] - prev_position >= distance:
                balls_count += 1
                prev_position = position[idx]

            if balls_count == m:
                return True

        return False

    output = -1
    position.sort()
    start, end = 1, (position[-1] - position[0]) // (m - 1) + 1
    while start <= end:
        mid = start + (end - start) // 2
        if is_possible(mid):
            output = mid
            start = mid + 1
        else:
            end = mid - 1

    return output
