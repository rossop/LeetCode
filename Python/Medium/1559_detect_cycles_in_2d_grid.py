"""
1559. Detect Cycles in 2D Grid

Given a 2D array of characters grid of size m x n, you need to find if there
exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the
same cell. From a given cell, you can move to one of the cells adjacent to it
in one of the four directions (up, down, left, or right), if it has the same
value of the current cell.

You cannot move to the cell that you visited in your last move. For example,
the cycle (1,1) -> (1,2) -> (1,1) is invalid because from (1,2) we revisited
the last cell.

Return true if any cycle of the same value exists in grid, otherwise false.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 500
- grid consists only of lowercase English letters.

Examples:

Example 1:
    Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
    Output: true

Example 2:
    Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
    Output: true

Example 3:
    Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
    Output: false
"""


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.setCount = n
        self.parent = list(range(n))
        self.size = [1] * n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> None:
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1

    def findAndUnite(self, x: int, y: int) -> bool:
        parentX, parentY = self.findset(x), self.findset(y)
        if parentX != parentY:
            self.unite(parentX, parentY)
            return True
        return False


class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        """
        Detects a cycle using Union-Find on the 2D grid flattened to 1D indices.

        Each cell (i, j) maps to index i*n + j. We scan left-to-right,
        top-to-bottom. For each cell we only check the two already-visited
        neighbours (up and left) that share the same character:
          - If they are already in the same component, adding this edge would
            close a cycle → return True.
          - Otherwise, unite their components.

        Checking only up and left is sufficient because right and down
        neighbours haven't been processed yet; their edges are handled when
        we reach those cells.

        Time complexity:  O(m * n * α(m * n)) — effectively O(m * n)
        Space complexity: O(m * n) for the Union-Find arrays
        """
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if not uf.findAndUnite(i * n + j, (i - 1) * n + j):
                        return True
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if not uf.findAndUnite(i * n + j, i * n + j - 1):
                        return True
        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            [["a", "a", "a", "a"], ["a", "b", "b", "a"],
             ["a", "b", "b", "a"], ["a", "a", "a", "a"]],
            True,
        ),
        (
            [["c", "c", "c", "a"], ["c", "d", "c", "c"],
             ["c", "c", "e", "c"], ["f", "c", "c", "c"]],
            True,
        ),
        (
            [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]],
            False,
        ),
        (
            [["a", "a"], ["a", "a"]],
            True,
        ),
        (
            [["a", "b"], ["b", "a"]],
            False,
        ),
    ]

    for grid, expected in test_cases:
        result = solution.containsCycle(grid)
        assert result == expected, \
            f"containsCycle failed: grid={grid} → expected {expected}, got {result}"
    print("All test cases passed!")
