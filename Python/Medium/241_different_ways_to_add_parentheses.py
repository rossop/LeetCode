"""
241. Different Ways to Add Parentheses

Problem Statement:
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

Example 1:
    Input: expression = "2-1-1"
    Output: [0,2]
    Explanation:
    ((2-1)-1) = 0 
    (2-(1-1)) = 2

Example 2:
    Input: expression = "2*3-4*5"
    Output: [-34,-14,-10,-10,10]
    Explanation:
    (2*(3-(4*5))) = -34 
    ((2*3)-(4*5)) = -14 
    ((2*(3-4))*5) = -10 
    (2*((3-4)*5)) = -10 
    (((2*3)-4)*5) = 10

Constraints:
- 1 <= expression.length <= 20
- expression consists of digits and the operator '+', '-', and '*'.
- All the integer values in the input expression are in the range [0, 99].
"""

from typing import List, Dict, Any


class Solution:
    """
    This class provides multiple methods to solve the 'Different Ways to Add Parentheses' problem.

    Each method explores different approaches to recursively evaluate all possible ways
    to group numbers and operators in the given expression and return all possible results.
    """

    # Dictionary of operations (standard method)
    operations: Dict[str, Any] = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }

    def compute_all_ways_recursive(self, expression: str) -> List[int]:
        """
        Computes different ways to group numbers and operators recursively.

        Time Complexity: O(4^n / n^(3/2)) due to the recursive nature of the solution and Catalan number complexity.
        Space Complexity: O(4^n / n^(3/2)) due to the recursive stack and the space required to store intermediate results.

        Args:
            expression: str - A string of digits and operators.

        Returns:
            List[int] - All possible results from evaluating the expression with different groupings.
        """
        res: List[int] = []

        for i in range(len(expression)):
            op = expression[i]
            if op in self.operations:
                nums1 = self.compute_all_ways_recursive(expression[:i])
                nums2 = self.compute_all_ways_recursive(expression[i + 1:])
                for n1 in nums1:
                    for n2 in nums2:
                        res.append(self.operations[op](n1, n2))

        if not res:
            res.append(int(expression))  # Base case when the expression contains only a number
        return res

    def compute_all_ways_backtrack(self, expression: str) -> List[int]:
        """
        Computes different ways to group numbers and operators using backtracking with explicit left and right indices.

        Time Complexity: O(4^n / n^(3/2)) due to the recursive nature and Catalan number complexity.
        Space Complexity: O(4^n / n^(3/2)) due to the recursive stack and intermediate results.

        Args:
            expression: str - A string of digits and operators.

        Returns:
            List[int] - All possible results from evaluating the expression with different groupings.
        """
        operations: Dict[str, Any] = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }

        def backtrack(left: int, right: int) -> List[int]:
            res: List[int] = []

            for i in range(left, right + 1):
                op = expression[i]
                if op in operations:
                    nums1 = backtrack(left, i - 1)
                    nums2 = backtrack(i + 1, right)
                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(operations[op](n1, n2))

            if not res:
                res.append(int(expression[left:right + 1]))
            return res

        return backtrack(0, len(expression) - 1)

    def compute_all_ways_memoized(self, expression: str) -> List[int]:
        """
        Computes different ways to group numbers and operators using memoization to avoid redundant calculations.

        Time Complexity: O(4^n / n^(3/2)) due to the recursive nature and Catalan number complexity.
        Space Complexity: O(4^n / n^(3/2)) due to the recursive stack and memoization table.

        Args:
            expression: str - A string of digits and operators.

        Returns:
            List[int] - All possible results from evaluating the expression with different groupings.
        """
        memo = {}
        return self._compute_results_memoized(expression, memo, 0, len(expression) - 1)

    def _compute_results_memoized(self, expression: str, memo: dict, start: int, end: int) -> List[int]:
        """
        Helper function to compute results with memoization to avoid redundant calculations.

        Time Complexity: O(4^n / n^(3/2)).
        Space Complexity: O(4^n / n^(3/2)).

        Args:
            expression: str - A string of digits and operators.
            memo: dict - A dictionary to store already computed results.
            start: int - Start index of the substring.
            end: int - End index of the substring.

        Returns:
            List[int] - All possible results for the current substring.
        """
        if (start, end) in memo:
            return memo[(start, end)]

        results = []

        if start == end:
            results.append(int(expression[start]))
            return results

        if end - start == 1 and expression[start].isdigit():
            results.append(int(expression[start:end + 1]))
            return results

        for i in range(start, end + 1):
            if expression[i].isdigit():
                continue

            left_results = self._compute_results_memoized(expression, memo, start, i - 1)
            right_results = self._compute_results_memoized(expression, memo, i + 1, end)

            for left_value in left_results:
                for right_value in right_results:
                    if expression[i] == "+":
                        results.append(left_value + right_value)
                    elif expression[i] == "-":
                        results.append(left_value - right_value)
                    elif expression[i] == "*":
                        results.append(left_value * right_value)

        memo[(start, end)] = results
        return results


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ("2-1-1", [0, 2]),
        ("2*3-4*5", [-34, -14, -10, -10, 10]),
        ("3", [3]),
        ("11+1", [12]),
        ("1+2+3", [6, 6])
    ]

    solution = Solution()

    for i, (expression, expected) in enumerate(test_cases):
        result = sorted(solution.compute_all_ways_recursive(expression))
        assert result == sorted(expected), f"Test case {i+1} failed for compute_all_ways_recursive: Expected {expected}, but got {result}"

        result2 = sorted(solution.compute_all_ways_memoized(expression))
        assert result2 == sorted(expected), f"Test case {i+1} failed for compute_all_ways_memoized: Expected {expected}, but got {result2}"

        result3 = sorted(solution.compute_all_ways_backtrack(expression))
        assert result3 == sorted(expected), f"Test case {i+1} failed for compute_all_ways_backtrack: Expected {expected}, but got {result3}"

    print("All test cases passed for all methods!")
