
"""
1905. Count Sub Islands

You are given two m x n binary matrices grid1 and grid2 containing only 0's 
(representing water) and 1's (representing land). An island is a group of 1's 
connected 4-directionally (horizontal or vertical). Any cells outside of the grid 
are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that 
contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Link: https://leetcode.com/problems/count-sub-islands/
"""
from typing import List, Set, Tuple

class Solution:
    """
    A class used to encapsulate the solution for the problem of counting sub-islands.

    The main strategy used is Depth First Search (DFS) to explore and identify islands 
    in grid2. For each island found in grid2, the algorithm checks if the corresponding 
    cells in grid1 also form an island. If so, it is counted as a sub-island.
    """

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        Count the number of sub-islands in grid2 that are fully contained in grid1.

        This method uses Depth First Search (DFS) to explore grid2 and determine if each
        island in grid2 is also present in grid1.

        Time Complexity: O(m * n)
            Each cell is visited at most once during the DFS traversal.

        Space Complexity: O(m * n)
            The maximum space used by the recursion stack and visited set.

        Args:
            grid1 (List[List[int]]): The reference grid containing the main islands.
            grid2 (List[List[int]]): The grid in which we need to count sub-islands.

        Returns:
            int: The number of sub-islands in grid2 that are fully contained in grid1.
        """

        ROWS: int = len(grid1)
        COLS: int = len(grid1[0])
        visit: Set[Tuple[int, int]] = set()

        def dfs(r: int, c: int) -> bool:
            """
            Perform a DFS to explore an island starting from cell (r, c) in grid2 and
            determine if it is a sub-island of grid1.

            Args:
                r (int): Row index of the current cell.
                c (int): Column index of the current cell.

            Returns:
                bool: True if the island in grid2 is a sub-island in grid1, False otherwise.
            """

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                grid2[r][c] == 0 or (r, c) in visit):
                return True
            
            visit.add((r, c))
            res = True  # Assume it is a sub-island unless proven otherwise

            if grid1[r][c] == 0:
                res = False

            # Explore all four directions
            res = dfs(r - 1, c) and res
            res = dfs(r + 1, c) and res
            res = dfs(r, c - 1) and res
            res = dfs(r, c + 1) and res

            return res

        count: int = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visit and dfs(r, c):
                    count += 1

        return count
    
    def countSubIslandsAlternative(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        An alternative method to count the number of sub-islands using an iterative DFS approach.

        This method also traverses grid2 to find islands, and checks against grid1 to ensure
        that the islands are sub-islands.

        Time Complexity: O(m * n)
            Each cell is visited at most once during the DFS traversal.

        Space Complexity: O(m * n)
            The maximum space used by the stack and visited set.

        Args:
            grid1 (List[List[int]]): The reference grid containing the main islands.
            grid2 (List[List[int]]): The grid in which we need to count sub-islands.

        Returns:
            int: The number of sub-islands in grid2 that are fully contained in grid1.
        """

        def dfs_iterative(r: int, c: int) -> bool:
            stack = [(r, c)]
            res = True

            while stack:
                x, y = stack.pop()

                if (x < 0 or y < 0 or x >= len(grid1) or y >= len(grid1[0]) or 
                    grid2[x][y] == 0 or (x, y) in visit):
                    continue

                visit.add((x, y))

                if grid1[x][y] == 0:
                    res = False

                # Add neighbors to the stack
                stack.append((x - 1, y))
                stack.append((x + 1, y))
                stack.append((x, y - 1))
                stack.append((x, y + 1))

            return res

        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()
        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and (r, c) not in visit and dfs_iterative(r, c):
                    count += 1

        return count

if __name__ == "__main__":
    test_cases = [
        ([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
         [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]], 3),
        ([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
         [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]], 2),
    ]

    solution = Solution()

    for i, (grid1, grid2, expected) in enumerate(test_cases):
        assert solution.countSubIslands(grid1, grid2) == expected, f"Test case {i + 1} failed"
        assert solution.countSubIslandsAlternative(grid1, grid2) == expected, f"Test case {i + 1} failed (Alternative)"
    
    print("All test cases passed!")