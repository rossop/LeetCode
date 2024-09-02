"""
This Python file provides a solution to the problem '1894. Find the Student
that Will Replace the Chalk' from LeetCode.

Problem: You are given a 0-indexed integer array 'chalk' representing the
amount of chalk each student uses and an integer 'k' representing the total
pieces of chalk available. The students are numbered from 0 to n-1. The teacher
will start giving problems to each student in turn, starting from student 0.
When a student cannot use the required chalk because it's less than what they
need, that student will be asked to replace the chalk. The task is to find out
which student will need to replace the chalk.

Constraints: - 1 <= n <= 10^5 - 1 <= chalk[i] <= 10^5 - 1 <= k <= 10^9

This file includes the main solution and a test suite to verify the correctness
of the implementation.
"""

from typing import List

class Solution:
    """
    Provides a method to find the student who will need to replace the chalk.
    """

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        """
        Finds the index of the student who will need to replace the chalk.

        Time Complexity: O(n) - Iterates through the chalk array twice.
        Space Complexity: O(1) - No extra space proportional to input size.

        Args:
            chalk (List[int]): Amount of chalk each student uses.
            k (int): Total amount of chalk available.

        Returns:
            int: Index of the student who will replace the chalk.
        """
        total_chalk = sum(chalk)
        k %= total_chalk
        
        for i, amount in enumerate(chalk):
            if k < amount:
                return i
            k -= amount


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([5, 1, 5], 22, 0),      # Example 1
        ([3, 4, 1, 2], 25, 1),   # Example 2
        ([1, 1, 1, 1], 4, 0),    # Example 3
    ]

    solution = Solution()

    for i, (chalk, k, expected) in enumerate(test_cases):
        result = solution.chalkReplacer(chalk, k)
        assert result == expected, \
            f"Test case {i+1} failed: Expected {expected}, but got {result}"

    print("All test cases passed!")
