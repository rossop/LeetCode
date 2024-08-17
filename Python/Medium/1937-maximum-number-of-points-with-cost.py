"""
1937. Maximum Number of Points with Cost
Link: https://leetcode.com/problems/maximum-number-of-points-with-cost/

This file contains a solution to the "Maximum Number of Points with Cost" problem. 
The problem is solved using Dynamic Programming (DP) with Tabulation. 
A brute-force version is also provided for comparison.
"""

from typing import List

class Solution:
    """
    Solution class for the "Maximum Number of Points with Cost" problem.

    This class provides two methods to solve the problem:
    1. `maxPoints`: A DP-based optimized approach with tabulation.
    2. `maxPointsBruteForce`: A brute-force approach that iterates over all possible changes.
    """

    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Dynamic Programming with Tabulation to maximize the points.

        This method iteratively calculates the maximum points that can be obtained 
        at each cell by considering the best possible cell from the previous row.

        Time Complexity: O(m * n)
        Space Complexity: O(n)

        Args:
            points (List[List[int]]): A 2D list representing the points grid.

        Returns:
            int: The maximum number of points that can be achieved.
        """
        R: int = len(points)
        C: int = len(points[0])
        row: List[int] = points[0].copy()

        for r in range(1, R):
            next_row: List[int] = points[r].copy()
            left: List[int] = [0] * C
            right: List[int] = [0] * C

            left[0] = row[0]
            for c in range(1, C):
                left[c] = max(row[c], left[c - 1] - 1)

            right[C - 1] = row[C - 1]
            for c in range(C - 2, -1, -1):
                right[c] = max(row[c], right[c + 1] - 1)

            for c in range(C):
                next_row[c] += max(left[c], right[c])
            row = next_row

        return max(row)

    def maxPointsBruteForce(self, points: List[List[int]]) -> int:
        """
        Brute Force approach to solve the Maximum Number of Points with Cost problem.

        This method iterates over all possible pairs of cells from adjacent rows 
        and computes the total score. It's less efficient and is used for comparison.

        Time Complexity: O((m * n) * n)
        Space Complexity: O(1)

        Args:
            points (List[List[int]]): A 2D list representing the points grid.

        Returns:
            int: The maximum number of points that can be achieved.
        """
        R: int = len(points)
        C: int = len(points[0])
        prev_row: List[int] = points[0].copy()

        for r in range(1, R):
            cur_row: List[int] = [0] * C
            for c1 in range(C):
                for c2 in range(C):
                    cur_row[c2] = max(cur_row[c2], prev_row[c1] + points[r][c2] - abs(c1 - c2))
            prev_row = cur_row

        return max(prev_row)


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([[1,2,3],[1,5,1],[3,1,1]], 9),  # Example 1
        ([[1,5],[2,3],[4,2]], 11),  # Example 2
        ([[0,0,0],[0,0,0],[0,0,0]], 0),  # Edge case: All zeros
        ([[100000]], 100000),  # Single cell grid
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 24),  # Larger grid
    ]

    methods = [
        solution.maxPoints,
        solution.maxPointsBruteForce,
    ]

    for method in methods:
        for i, (points, expected) in enumerate(test_cases, 1):
            result = method(points)
            assert result == expected, f"Test case {i} failed for {method.__name__}: expected {expected}, got {result}"

    print("All test cases passed!")