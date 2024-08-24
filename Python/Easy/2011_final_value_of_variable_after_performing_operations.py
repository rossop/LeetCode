"""
2011. Final Value of Variable After Performing Operations

There is a programming language with only four operations and one variable X:

- ++X and X++ increments the value of the variable X by 1.
- --X and X-- decrements the value of the variable X by 1.

Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return
the final value of X after performing all the operations.

Problem Link:
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

Examples:
    Example 1:
        Input: operations = ["--X","X++","X++"]
        Output: 1
        Explanation: The operations are performed as follows:
        Initially, X = 0.
        --X: X is decremented by 1, X =  0 - 1 = -1.
        X++: X is incremented by 1, X = -1 + 1 =  0.
        X++: X is incremented by 1, X =  0 + 1 =  1.

    Example 2:
        Input: operations = ["++X","++X","X++"]
        Output: 3
        Explanation: The operations are performed as follows:
        Initially, X = 0.
        ++X: X is incremented by 1, X = 0 + 1 = 1.
        ++X: X is incremented by 1, X = 1 + 1 = 2.
        X++: X is incremented by 1, X = 2 + 1 = 3.

    Example 3:
        Input: operations = ["X++","++X","--X","X--"]
        Output: 0
        Explanation: The operations are performed as follows:
        Initially, X = 0.
        X++: X is incremented by 1, X = 0 + 1 = 1.
        ++X: X is incremented by 1, X = 1 + 1 = 2.
        --X: X is decremented by 1, X = 2 - 1 = 1.
        X--: X is decremented by 1, X = 1 - 1 = 0.

Constraints:
    1 <= operations.length <= 100
    operations[i] will be either "++X", "X++", "--X", or "X--".
"""

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        Direct approach using a loop to evaluate the final value of X.

        Time Complexity: O(n), where n is the length of the operations list.
        Space Complexity: O(1), as only a few additional variables are used.

        Args:
            operations (List[str]): List of operations to perform on X.

        Returns:
            int: The final value of X after all operations.
        """
        ans: int = 0
        for op in operations:
            if '+' in op:
                ans += 1
            if '-' in op:
                ans -= 1
        return ans

    def finalValueAfterOperationsWithMap(self, operations: List[str]) -> int:
        """
        Attempted approach using map to evaluate the final value of X.
        However, this version is incorrect due to the misuse of map and sum
        functions.

        Time Complexity: O(n), where n is the length of the operations list.
        Space Complexity: O(1), as only a few additional variables are used.

        Args:
            operations (List[str]): List of operations to perform on X.

        Returns:
            int: The final value of X after all operations.
        """
        def eval_(op: str) -> int:
            if '+' in op:
                return 1
            if '-' in op:
                return -1
            return 0

        return sum(map(eval_, operations))

    def finalValueAfterOperationsComp(self, operations: List[str]) -> int:
        """
        A more concise implementation using list comprehension and sum.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        return sum(1 if '+' in op else -1 for op in operations)


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (["--X", "X++", "X++"], 1),
        (["++X", "++X", "X++"], 3),
        (["X++", "++X", "--X", "X--"], 0),
        (["++X"], 1),
        (["--X", "--X", "--X"], -3)
    ]

    for ops, expected in test_cases:
        # Test the direct loop method
        result = solution.finalValueAfterOperations(ops)
        assert result == expected, f"""
        Direct loop method failed: expected {expected}, got {result}
        """

        # Test the map method
        result_map = solution.finalValueAfterOperationsWithMap(ops)
        assert result_map == expected, f"""
        Map method failed: expected {expected}, got {result_map}
        """

    print("All test cases passed!")
