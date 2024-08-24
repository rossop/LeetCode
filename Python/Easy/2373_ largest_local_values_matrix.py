"""
2373. Largest Local Values in a Matrix

You are given an n x n integer matrix grid. Generate an integer matrix maxLocal
of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid
centered around row i + 1 and column j + 1.

In other words, we want to find the largest value in every contiguous 3 x 3
matrix in grid. Return the generated matrix.

Constraints:
- n == grid.length == grid[i].length
- 3 <= n <= 100
- 1 <= grid[i][j] <= 100

Example 1:

Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated
matrix. Notice that each value in the generated matrix corresponds to the
largest value of a contiguous 3 x 3 matrix in grid.

Example 2:

Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3
matrix in grid.
"""
from typing import List


class Solution:
    """
    A class used to encapsulate the solution for finding the largest local values in a matrix.

    Given an n x n integer matrix grid, the class generates an integer matrix maxLocal of size
    (n - 2) x (n - 2) such that each element maxLocal[i][j] is equal to the largest value in
    the 3 x 3 matrix centered around row i + 1 and column j + 1 in the grid.

    The goal is to find the largest value in every contiguous 3 x 3 submatrix within the grid.
    """

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Compute the largest local values in a grid.

        This method takes a grid as input and returns a matrix representing the largest values 
        within every 3 x 3 submatrix in the grid.

        Args:
            grid (List[List[int]]): A 2D list representing an n x n matrix.

        Returns:
            List[List[int]]: A 2D list representing the largest local values in the grid.
        """
        m: int = len(grid)
        n: int = len(grid[0])
        ans: List[List[int]] = [[0 for _ in range(n-2)] for _ in range(m-2)]

        for i in range(1, m-1):
            for j in range(1, n-1):
                submask = [grid[i-1][j-1], grid[i][j-1], grid[i+1][j-1],
                           grid[i-1][j], grid[i][j], grid[i+1][j],
                           grid[i-1][j+1], grid[i][j+1], grid[i+1][j+1]]
                ans[i-1][j-1] = max(submask)

        return ans


    def largestLocalAlt(self, grid: List[List[int]]) -> List[List[int]]:
        """
        An alternative approach to compute the largest local values in a grid.

        This alternative solution iterates over the grid and directly compares the values 
        in the 3 x 3 submatrices, updating the result matrix in a more streamlined fashion.

        Args:
            grid (List[List[int]]): A 2D list representing an n x n matrix.

        Returns:
            List[List[int]]: A 2D list representing the largest local values in the grid.
        """
        n: int = len(grid)
        result: List[List[int]] = []

        for i in range(n - 2):
            row: List[int] = []
            for j in range(n - 2):
                max_val = max(grid[i][j], grid[i][j + 1], grid[i][j + 2],
                              grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                              grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2])
                row.append(max_val)
            result.append(row)

        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (Input, Expected Output)
        ([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]], [[9, 9], [8, 6]]),
        ([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]])
    ]

    for i, (grid, expected) in enumerate(test_cases):
        assert solution.largestLocal(grid) == expected, f"Test case {i + 1} failed for largestLocal."
        assert solution.largestLocalAlt(grid) == expected, f"Test case {i + 1} failed for largestLocalAlt."

    print("All tests passed!")
