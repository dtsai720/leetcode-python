def student_attendance_record_ii(n: int) -> int:
    """
    This function calculates the number of possible attendance records of length 'n'.
    An attendance record is a string that only contains the following three characters:
    'A' : Absent.
    'L' : Late.
    'P' : Present.
    A record is regarded as rewardable if it doesn't contain more than one 'A' (absent)
    or more than two continuous 'L' (late).

    Args:
        n: int : Length of the attendance record

    Returns:
        int : Number of possible attendance records of length 'n'
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    mod = 1e9 + 7
    max_absent = 2
    max_late = 3
    dp = [[[0] * max_late for _ in range(max_absent)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(n):
        for absent in range(max_absent):
            for late in range(max_late):
                dp[i + 1][absent][0] = (
                    dp[i + 1][absent][0] + dp[i][absent][late]
                ) % mod

                if absent < 1:
                    dp[i + 1][absent + 1][0] = (
                        dp[i + 1][absent + 1][0] + dp[i][absent][late]
                    ) % mod
                if late < 2:
                    dp[i + 1][absent][late + 1] = (
                        dp[i + 1][absent][late + 1] + dp[i][absent][late]
                    ) % mod
    output = 0
    for absent in range(max_absent):
        for late in range(max_late):
            output = (output + dp[n][absent][late]) % mod
    return output
