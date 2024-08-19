"""
650. 2 Keys Keyboard
Link: https://leetcode.com/problems/2-keys-keyboard/

There is only one character 'A' on the screen of a notepad. You can perform one
of two operations on this notepad for each step:
1. Copy All: You can copy all the characters present on the screen (a partial
    copy is not allowed).
2. Paste: You can paste the characters which are copied last time.

Given an integer n, return the minimum number of operations to get the
character 'A' exactly n times on the screen.

Example 1:
Input: n = 3
Output: 3
Explanation:
Step 1: Copy All -> A
Step 2: Paste -> AA
Step 3: Paste -> AAA

Example 2:
Input: n = 1
Output: 0

Constraints:
1 <= n <= 1000
"""

from typing import List, Dict


class Solution:
    """
    Solution class for solving the 2 Keys Keyboard problem using different
    approaches.
    """

    def minStepsDP(self, n: int) -> int:
        """
        Dynamic Programming (Tabulation) solution to find the minimum number
        of steps to get 'A' exactly n times.

        Time Complexity: O(n^2)
        Space Complexity: O(n)

        Args:
            n (int): The target number of 'A's.

        Returns:
            int: Minimum number of operations required.
        """
        dp: List[int] = [float('inf')] * (n + 1)
        dp[1] = 0

        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n]

    def minStepsMemoization(self, n: int) -> int:
        """
        Dynamic Programming (Memoization) solution to find the minimum number
        of steps to get 'A' exactly n times.

        Time Complexity: O(n^2)
        Space Complexity: O(n)

        Args:
            n (int): The target number of 'A's.

        Returns:
            int: Minimum number of operations required.
        """
        memo: Dict[int, int] = {1: 0}

        def dp(x: int) -> int:
            if x in memo:
                return memo[x]
            min_steps = x  # Max possible steps
            for i in range(1, x // 2 + 1):
                if x % i == 0:
                    min_steps = min(min_steps, dp(i) + x // i)
            memo[x] = min_steps
            return min_steps

        return dp(n)

    def minStepsFactorization(self, n: int) -> int:
        """
        Optimized solution using prime factorization to find the minimum number
        of steps.

        Time Complexity: O(sqrt(n))
        Space Complexity: O(1)

        Args:
            n (int): The target number of 'A's.

        Returns:
            int: Minimum number of operations required.
        """
        steps = 0
        divisor = 2

        while n > 1:
            while n % divisor == 0:
                steps += divisor
                n //= divisor
            divisor += 1

        return steps


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (3, 3),  # Example 1
        (1, 0),  # Example 2
        (4, 4),  # Test for n = 4
        (5, 5),  # Test for n = 5
        (6, 5),  # Test for n = 6
        (100, 14),  # Larger test case
        (1000, 21)  # Upper limit test case
    ]

    methods = [
        solution.minStepsDP,
        solution.minStepsMemoization,
        solution.minStepsFactorization
    ]

    for method in methods:
        for ii, (num, expected) in enumerate(test_cases, 1):
            result = method(num)
            assert result == expected, \
                f"Test case {ii} failed for {method.__name__}: \
                expected {expected}, got {result}"

    print("All test cases passed!")
