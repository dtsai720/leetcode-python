from typing import List


def coin_change_ii(coins: List[int], amount: int) -> int:
    """
    You are given coins of different denominations and a total amount of money.
    Write a function to compute the number of combinations that make up that amount.
    You may assume that you have infinite number of each kind of coin.

    Args:
        coins: List[int] - List of coin denominations
        amount: int - Total amount of money

    Returns:
        int - Number of combinations that make up the amount
    """
    if not (
        isinstance(coins, list)
        and all(isinstance(coin, int) for coin in coins)
        and isinstance(amount, int)
    ):
        raise TypeError(
            "coins must be a list of integers and amount must be an integer"
        )

    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]
