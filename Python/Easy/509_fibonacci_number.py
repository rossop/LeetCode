"""
509. Fibonacci Number
Link: https://leetcode.com/problems/fibonacci-number/

This file contains various solutions to the "Fibonacci Number" problem. The Fibonacci sequence is a series 
of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1. The task is to 
compute the nth Fibonacci number. Multiple methods are provided, including dynamic programming (both top-down 
and bottom-up), memoization, a mathematical approach using the golden ratio, and a recursive solution.
"""

from typing import List, Dict

class Solution:
    """
    Solution class for the "Fibonacci Number" problem.

    This class provides multiple methods to compute the nth Fibonacci number using different approaches:
    1. `fibGoldenRatio`: Uses the mathematical formula involving the golden ratio.
    2. `fib`: Optimized bottom-up approach with constant space.
    3. `fibTabulation`: Bottom-up approach using a table to store intermediate results.
    4. `fibMemoisation`: Top-down approach with memoization.
    5. `fibRecursive`: Simple recursive approach (inefficient for large n).
    """

    def fibGoldenRatio(self, n: int) -> int:
        """
        Computes the nth Fibonacci number using the golden ratio formula.

        This method uses the closed-form expression known as Binet's formula, 
        which approximates Fibonacci numbers using the golden ratio.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Args:
            n (int): The position in the Fibonacci sequence to compute.

        Returns:
            int: The nth Fibonacci number.
        """
        golden_ratio = (1 + (5 ** 0.5)) / 2
        return int(round((golden_ratio ** n) / (5 ** 0.5)))

    def fib(self, n: int) -> int:
        """
        Computes the nth Fibonacci number using an optimized bottom-up approach.

        This method uses a constant amount of space by only keeping track of the 
        last two Fibonacci numbers.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            n (int): The position in the Fibonacci sequence to compute.

        Returns:
            int: The nth Fibonacci number.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev: int = 0
        cur: int = 1

        for i in range(2, n + 1):
            prev, cur = cur, prev + cur
        
        return cur

    def fibTabulation(self, n: int) -> int:
        """
        Computes the nth Fibonacci number using a bottom-up tabulation approach.

        This method fills up a table with Fibonacci values from the base cases 
        up to the nth number.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Args:
            n (int): The position in the Fibonacci sequence to compute.

        Returns:
            int: The nth Fibonacci number.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp: List[int] = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

    def fibMemoisation(self, n: int) -> int:
        """
        Computes the nth Fibonacci number using a top-down memoization approach.

        This method applies dynamic programming by storing intermediate results 
        to avoid recalculating them.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Args:
            n (int): The position in the Fibonacci sequence to compute.

        Returns:
            int: The nth Fibonacci number.
        """
        memo: Dict[int, int] = {0: 0, 1: 1}

        def f(x: int) -> int:
            if x in memo:
                return memo[x]
            memo[x] = f(x - 1) + f(x - 2)
            return memo[x]
        
        return f(n)

    def fibRecursive(self, n: int) -> int:
        """
        Computes the nth Fibonacci number using a simple recursive approach.

        This method directly implements the recursive definition of the Fibonacci 
        sequence. It is inefficient for large n due to overlapping subproblems.

        Time Complexity: O(2^n)
        Space Complexity: O(n) for the recursion stack.

        Args:
            n (int): The position in the Fibonacci sequence to compute.

        Returns:
            int: The nth Fibonacci number.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibRecursive(n - 1) + self.fibRecursive(n - 2)


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (2, 1),  # F(2) = 1
        (3, 2),  # F(3) = 2
        (4, 3),  # F(4) = 3
        (10, 55),  # F(10) = 55
        (30, 832040),  # F(30) = 832040
        (0, 0),  # F(0) = 0 (Edge case)
        (1, 1),  # F(1) = 1 (Edge case)
    ]

    methods = [
        solution.fibGoldenRatio,
        solution.fib,
        solution.fibTabulation,
        solution.fibMemoisation,
        solution.fibRecursive
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        for method in methods:
            result = method(n)
            assert result == expected, f"Test case {i} failed for {method.__name__}: expected {expected}, got {result}"

    print("All test cases passed!")