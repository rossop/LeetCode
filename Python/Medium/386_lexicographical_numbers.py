"""
386. Lexicographical Numbers

Problem Statement:
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

Constraints:
- 1 <= n <= 5 * 10^4

Example 1:
    Input: n = 13
    Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

Example 2:
    Input: n = 2
    Output: [1, 2]
"""

from typing import List, Optional

class Solution:
    """
    This class contains three methods to solve the problem of generating numbers in the range [1, n]
    sorted in lexicographical order.

    Methods:
    1. lexicalOrderIterative: Iterative approach using greedy logic.
    2. lexicalOrderDFS: Recursive DFS approach.
    3. lexicalOrderFlatten: Flattening approach with sorting using a custom comparator.

    - The iterative and DFS methods aim to meet the O(n) time complexity requirement.
    - The flatten approach is more intuitive but does not meet the O(n) time complexity requirement due to sorting.

    Comparison:
    - `lexicalOrderIterative` has the best performance with O(n) time and O(1) extra space.
    - `lexicalOrderDFS` is also efficient but requires O(n) space due to recursion.
    - `lexicalOrderFlatten` uses sorting and therefore runs in O(n log n) time with O(n) space.
    """

    def lexicalOrderIterative(self, n: int) -> List[int]:
        """
        Iterative method to generate lexicographical numbers.

        Time Complexity: O(n), where n is the number of integers to generate.
        Space Complexity: O(1) extra space (excluding the result list).

        Args:
            n: int - The upper limit of the range.

        Returns:
            List[int] - A list of numbers sorted in lexicographical order.
        """
        res: List[int] = []
        cur: int = 1

        while len(res) < n:
            res.append(cur)

            # Move to the next number in lexicographical order
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur == n or cur % 10 == 9:
                    cur //= 10
                cur += 1

        return res

    def lexicalOrderDFS(self, n: int) -> List[int]:
        """
        DFS method to generate lexicographical numbers.

        Time Complexity: O(n), where n is the number of integers to generate.
        Space Complexity: O(n), due to the call stack used in recursion.

        Args:
            n: int - The upper limit of the range.

        Returns:
            List[int] - A list of numbers sorted in lexicographical order.
        """
        res = []

        def dfs(cur: int) -> Optional[List[int]]:
            if cur > n:
                return
            res.append(cur)
            cur *= 10
            for i in range(10):
                dfs(cur + i)

        for i in range(1, 10):
            dfs(i)
        
        return res 

    def lexicalOrderFlatten(self, n: int) -> List[int]:
        """
        Flatten approach to generate lexicographical numbers by sorting.

        Time Complexity: O(n log n), due to sorting.
        Space Complexity: O(n), due to the space used to store the numbers and sorting.

        Args:
            n: int - The upper limit of the range.

        Returns:
            List[int] - A list of numbers sorted in lexicographical order.
        """
        if n < 9:
            return list(range(1, n + 1))

        def flatten(i: int) -> float:
            # Flatten the number by reducing it to a single-digit representative
            while i >= 10:
                i /= 10
            return i
        
        ans: List[int] = list(range(1, n + 1))
        
        return sorted(ans, key=flatten)


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        (13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]),
        (2, [1, 2]),
        (25, [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 3, 4, 5, 6, 7, 8, 9]),
    ]

    solution = Solution()

    print("Testing lexicalOrderIterative:")
    for i, (n, expected) in enumerate(test_cases):
        result = solution.lexicalOrderIterative(n)
        assert result == expected, f"Test case {i+1} failed (Iterative): Expected {expected}, but got {result}"
    print("All test cases passed for lexicalOrderIterative!")

    print("\nTesting lexicalOrderDFS:")
    for i, (n, expected) in enumerate(test_cases):
        result = solution.lexicalOrderDFS(n)
        assert result == expected, f"Test case {i+1} failed (DFS): Expected {expected}, but got {result}"
    print("All test cases passed for lexicalOrderDFS!")

    print("\nTesting lexicalOrderFlatten:")
    for i, (n, expected) in enumerate(test_cases):
        result = solution.lexicalOrderFlatten(n)
        assert result == expected, f"Test case {i+1} failed (Flatten): Expected {expected}, but got {result}"
    print("All test cases passed for lexicalOrderFlatten!")
