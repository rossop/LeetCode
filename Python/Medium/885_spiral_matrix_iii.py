"""
885. Spiral Matrix III
Link: https://leetcode.com/problems/spiral-matrix-iii/

You start at the cell (rStart, cStart) of an rows x cols grid facing east.
The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid.
Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later).
Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

Example 1:
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],
         [3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],
         [4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],
         [2,0],[1,0],[0,0]]

Constraints:
1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols

TOPICS: Array, Matrix, Simulation
"""

from typing import List

class Solution:
    """
    Solution class for the Spiral Matrix III problem.

    The solution generates the coordinates of the grid in a spiral order starting from (rStart, cStart).
    """

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        """
        Returns the coordinates of the grid in spiral order starting from (rStart, cStart).

        This method uses a spiral traversal technique with efficient boundary checking.

        Time Complexity: O(rows * cols)
        Space Complexity: O(1) - ignoring the output list size

        Args:
            rows (int): Number of rows in the grid.
            cols (int): Number of columns in the grid.
            rStart (int): Starting row index.
            cStart (int): Starting column index.

        Returns:
            List[List[int]]: List of coordinates visited in spiral order.
        """
        # Directions: right, down, left, up
        direction: List[List[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r, c = rStart, cStart
        spiral: List[List[int]] = [[r, c]]
        steps = 1  # Start with 1 step in each direction

        while len(spiral) < rows * cols:
            for d in range(4):  # 4 directions
                for _ in range(steps):
                    r += direction[d][0]
                    c += direction[d][1]
                    if 0 <= r < rows and 0 <= c < cols:
                        spiral.append([r, c])
                # Increase steps after right (d == 1) and left (d == 3)
                if d == 1 or d == 3:
                    steps += 1
        
        return spiral


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (1, 4, 0, 0, [[0, 0], [0, 1], [0, 2], [0, 3]]),  # Example 1
        (5, 6, 1, 4, [
            [1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5],
            [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4],
            [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0],
            [2, 0], [1, 0], [0, 0]
        ]),  # Example 2
    ]

    for i, (rows, cols, rStart, cStart, expected) in enumerate(test_cases, 1):
        result = solution.spiralMatrixIII(rows, cols, rStart, cStart)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    
    print("All test cases passed!")