"""
200. Number of Islands
Link: https://leetcode.com/problems/number-of-islands/

This file contains a solution to the "Number of Islands" problem. The solution is implemented 
in the `Solution` class, which provides a method to determine the number of islands in a given 
2D binary grid. An island is formed by connecting adjacent lands horizontally or vertically. 
The method uses Depth-First Search (DFS) to traverse the grid and count the number of distinct islands.
"""

from typing import List

class Solution:
    """
    Solution class for the "Number of Islands" problem.

    This class provides a method to count the number of islands in a 2D binary grid. 
    An island is surrounded by water and is formed by connecting adjacent lands ('1') 
    horizontally or vertically. The method uses a Depth-First Search (DFS) approach 
    to explore and mark each island in the grid.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Counts the number of islands in the given 2D binary grid.

        The method uses Depth-First Search (DFS) to traverse each island and marks 
        the visited lands as water ('0') to avoid counting them again. The traversal 
        continues until all lands are visited, and the total number of islands is returned.

        Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
        Space Complexity: O(m * n) in the worst case for the recursion stack if the grid is filled with land.

        Args:
            grid (List[List[str]]): A 2D binary grid where '1' represents land and '0' represents water.

        Returns:
            int: The number of islands in the grid.
        """
        M: int = len(grid)
        N: int = len(grid[0])
        num_islands: int = 0

        def dfs(i: int, j: int):
            """
            Depth-First Search to traverse and mark the connected lands as water.

            Args:
                i (int): The row index of the current cell.
                j (int): The column index of the current cell.
            """
            if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            dfs(i, j + 1)  # right
            dfs(i, j - 1)  # left
            dfs(i + 1, j)  # down
            dfs(i - 1, j)  # up

        for m in range(M):
            for n in range(N):
                if grid[m][n] == "1":
                    num_islands += 1
                    dfs(m, n)
        return num_islands


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ], 1),  # Example 1

        ([
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ], 3),  # Example 2

        ([
            ["1","0","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","0","1"]
        ], 3),  # Additional case: Diagonal islands should not be connected

        ([
            ["0","0","0","0","0"],
            ["0","0","0","0","0"],
            ["0","0","0","0","0"]
        ], 0),  # Edge case: No islands

        ([
            ["1","1","1","1","1"],
            ["1","1","1","1","1"],
            ["1","1","1","1","1"]
        ], 1)  # Edge case: Single large island
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        result = solution.numIslands(grid)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")