def number_of_steps_to_reduce_a_number_in_binary_representation_to_one(s: str) -> int:
    """
    Given a number s in binary representation, return the number of steps to
    reduce it to one under the following rules:
    - If the current number is even, you have to divide it by 2.
    - If the current number is odd, you have to add 1 to it.

    Args:
        s: str : Binary representation of a number

    Returns:
        int : Number of steps to reduce the number to one
    """

    if not isinstance(s, str):
        raise TypeError("s must be a string")

    count, carry = 0, 0
    for i in range(len(s) - 1, 0, -1):
        if (ord(s[i]) - ord("0") + carry) % 2 == 1:
            count += 2
            carry = 1
        else:
            count += 1

    return count + carry
