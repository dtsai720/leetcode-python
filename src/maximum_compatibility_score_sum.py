from typing import List


def maximum_compatibility_score_sum(
    students: List[List[int]], mentors: List[List[int]]
) -> int:
    """
    Given two lists of integers students and mentors, where students[i] is the compatibility of
    student i and mentors[j] is the compatibility of mentor j,
    return the maximum compatibility score sum of the students assigned to the mentors.

    Each student is assigned to one mentor and each mentor is assigned to one student.

    The compatibility score of a student-mentor pair is the number of answers they agree on.

    Args:
        students (List[List[int]]): a list of integers representing the compatibility of students
        mentors (List[List[int]]): a list of integers representing the compatibility of mentors

    Returns:
        int - the maximum compatibility score sum of the students assigned to the mentors
    """
    if not (
        isinstance(students, list)
        and isinstance(mentors, list)
        and all(
            isinstance(student, list) and isinstance(mentor, list)
            for student, mentor in zip(students, mentors)
        )
        and all(
            all(isinstance(x, int) for x in student)
            and all(isinstance(x, int) for x in mentor)
            for student, mentor in zip(students, mentors)
        )
    ):
        raise TypeError("students and mentors must be a list of integers")

    if len(students) != len(mentors):
        raise ValueError("students and mentors must have the same length")

    n = len(students)
    m = len(students[0])

    array = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(students[i]) != len(mentors[j]):
                raise ValueError("students and mentors must have the same length")

            array[i][j] = sum(students[i][k] == mentors[j][k] for k in range(m))

    visited = [False] * n
    output = 0

    def _helper(idx: int, current: int) -> None:
        if idx == n:
            nonlocal output
            output = max(output, current)
            return

        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            _helper(idx + 1, current + array[idx][i])
            visited[i] = False

    _helper(0, 0)

    return output
