"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

This problem is equivalent to finding the nth number in the Fibonacci sequence,
where F(1) = 1, F(2) = 2, and F(n) = F(n-1) + F(n-2) for n > 2.

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""

from typing import List


class Solution:
    """
    This class contains methods to solve the 'Climbing Stairs' problem using
    different approaches: Dynamic Programming and a Combinatorial method.

    Comparison of Methods:
    - The Dynamic Programming approach (climbStairs) is more efficient in terms
      of both time and space, with O(n) time complexity and O(1) space
      complexity.
    - The Combinatorial approach (climbStairsFactorial) is less efficient, with
      O(n^2) time complexity and O(n) space complexity, but provides an
      interesting mathematical perspective on the problem.
    """

    def climbStairs(self, n: int) -> int:
        """
        Dynamic Programming (Bottom-up) approach to solve the Climbing Stairs
        problem.

        This approach uses O(1) space and O(n) time to calculate the number of
        distinct ways to reach the top of the staircase.

        Args:
            n (int): The number of steps to reach the top.

        Returns:
            int: The number of distinct ways to climb to the top.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prev1, prev2 = 2, 1

        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1

    def climbStairsFactorial(self, n: int) -> int:
        """
        Combinatorial approach to solve the Climbing Stairs problem.

        This approach calculates the number of distinct ways by considering the
        number of ways to arrange combinations of 1-step and 2-step moves.

        Args:
            n (int): The number of steps to reach the top.

        Returns:
            int: The number of distinct ways to climb to the top.

        Time Complexity: O(n^2)
        Space Complexity: O(n)

        Note: This approach is less efficient than the dynamic programming
        solution, especially for larger values of n.
        """
        factorials: List[int] = [1, 1]

        def factorial(i: int) -> int:
            num_of_factorials = len(factorials)
            if i < num_of_factorials:
                return factorials[i]

            for j in range(num_of_factorials, i + 1):
                f = factorials[-1] * j
                factorials.append(f)
            return factorials[i]

        m = n // 2
        summ: int = 0
        for x in range(m+1):
            y: int = n - 2*x
            summ += factorial(x+y)//(factorial(x)*factorial(y))

        return summ


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (2, 2),   # 2 ways: (1+1), (2)
        (3, 3),   # 3 ways: (1+1+1), (1+2), (2+1)
        (4, 5),   # 5 ways: (1+1+1+1), 3x (1,1,2), (2+2)
        (5, 8),   # 8 ways: (1+1+1+1+1), 3x (1,1,1,2), 3x (2,2,1)
        (10, 89)  # 89 ways (Fibonacci sequence)
    ]

    for num, expected in test_cases:
        result = solution.climbStairs(num)
        assert result == expected, f"""
            Test case failed for n={num}.
            Expected {expected}, got {result}
            """

        result_factorial = solution.climbStairsFactorial(num)
        assert result_factorial == expected, f"""
            Test case failed for n={num} with factorial approach.
            Expected {expected}, got {result_factorial}
            """

    print("All test cases passed!")
