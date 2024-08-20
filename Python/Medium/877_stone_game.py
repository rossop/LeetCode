"""
877. Stone Game
Link: https://leetcode.com/problems/stone-game/

Alice and Bob play a game with piles of stones. There are an even number of
piles arranged in a row,
and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of
stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes
the entire pile of stones either from the beginning or from the end of the row.
This continues until there are no more piles left, at which point the person
with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or
false if Bob wins.

Example 1:
Input: piles = [5, 3, 4, 5]
Output: true

Example 2:
Input: piles = [3, 7, 2, 3]
Output: true

Constraints:
2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.
"""

from typing import List

class Solution:
    def stoneGameDP(self, piles: List[int]) -> bool:
        """
        Dynamic Programming Approach:
        This approach uses a 2D DP table to simulate the game and calculate
        the maximum stones Alice can get over Bob
        by considering all possible moves.

        Time Complexity: O(n^2)
        Space Complexity: O(n^2)

        Args:
            piles (List[int]): The list of stone piles.

        Returns:
            bool: True if Alice can win, False otherwise.
        """
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                                piles[i] - dp[i + 1][j],
                                piles[j] - dp[i][j - 1]
                                )

        return dp[0][n - 1] > 0

    def stoneGameTwoPointers(self, piles: List[int]) -> bool:
        """
        Two-Pointer Approach:
        Alice and Bob pick stones from either end of the row. Since they both
        play optimally, this approach simulates the decision-making process
        for both players.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            piles (List[int]): The list of stone piles.

        Returns:
            bool: True since Alice will always win with optimal play.

        NOTE: something is odd with this anwer, it solved the problem, then
            I rerun it later and it returned errors
        """
        n: int = len(piles)
        left: int = 0
        right: int = n - 1
        alice_count: int = 0
        bob_count: int = 0
        i: int = 0

        while left < right:
            if i % 2 == 0:  # Alice goes
                val: int = max(piles[right], piles[left])
                if max(piles[right], piles[left]) == piles[right]:
                    right -= 1
                else:
                    left += 1
                alice_count += val
            else:  # Bob goes
                val: int = max(piles[right], piles[left])
                if max(piles[right], piles[left]) == piles[right]:
                    right -= 1
                else:
                    left += 1
                bob_count += val

        return alice_count > bob_count


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([5, 3, 4, 5], True),  # Example 1
        ([3, 7, 2, 3], True),  # Example 2
        ([3, 2, 10, 4], True),  # Custom Test 1
        ([8, 15, 3, 7], True),  # Custom Test 2
    ]

    methods = [
        solution.stoneGameDP,
        solution.stoneGameTwoPointers
    ]

    for method in methods:
        for k, (input_piles, expected) in enumerate(test_cases, 1):
            result = method(input_piles)
            assert result == expected, f"Test case {k} failed for \
                {method.__name__}: expected {expected}, got {result}"

    print("All test cases passed!")
