"""
1861. Rotating the Box

You are given an m x n matrix of characters boxGrid representing a side-view
of a box. Each cell of the box is one of the following:
    - A stone '#'
    - A stationary obstacle '*'
    - Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall
due to gravity. Each stone falls down until it lands on an obstacle, another
stone, or the bottom of the box. Gravity does not affect the obstacles'
positions, and the inertia from the box's rotation does not affect the
stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another
stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described
above.

Constraints:
- m == boxGrid.length
- n == boxGrid[i].length
- 1 <= m, n <= 500
- boxGrid[i][j] is either '#', '*', or '.'.

Examples:

Example 1:
    Input:  boxGrid = [["#", ".", "#"]]
    Output: [["."], ["#"], ["#"]]

Example 2:
    Input:  boxGrid = [["#", ".", "*", "."],
                       ["#", "#", "*", "."]]
    Output: [["#", "."],
             ["#", "#"],
             ["*", "*"],
             [".", "."]]

Example 3:
    Input:  boxGrid = [["#", "#", "*", ".", "*", "."],
                       ["#", "#", "#", "*", ".", "."],
                       ["#", "#", "#", ".", "#", "."]]
    Output: [[".", "#", "#"],
             [".", "#", "#"],
             ["#", "#", "*"],
             ["#", "*", "."],
             ["#", ".", "*"],
             ["#", ".", "."]]
"""

import copy


class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        """
        Settles stones in the un-rotated frame, then rotates 90° clockwise.

        Trick: rotating first would force gravity to act along columns, which
        is awkward in a row-major grid. Instead we treat "down" (post-rotation)
        as "right" (pre-rotation) and slide stones along each row to the right
        before rotating the grid.

        Two pointers per row, scanning right to left:
            - p scans every cell.
            - c marks the next available landing slot for a falling stone.
        On '#' we move the stone from p into c, then decrement c.
        On '*' we reset c to p - 1 — the next stone must land left of the
        obstacle.
        On '.' we keep scanning.

        Time complexity:  O(m * n)
        Space complexity: O(m * n) — for the rotated output (in-place fall,
                          new matrix only for the rotation).
        """
        cols: int = len(boxGrid[0])

        for r in range(len(boxGrid)):
            c: int = cols - 1
            for p in range(cols - 1, -1, -1):
                if boxGrid[r][p] == '#':
                    boxGrid[r][p] = '.'
                    boxGrid[r][c] = '#'
                    c -= 1
                elif boxGrid[r][p] == '*':
                    c = p - 1

        return [list(row) for row in zip(*boxGrid[::-1])]

    def rotateTheBoxWhile(self, boxGrid: list[list[str]]) -> list[list[str]]:
        """
        Same algorithm expressed with an explicit while loop.

        The for-loop variant is preferred — it makes the invariant "p sweeps
        every column once" obvious. This version is kept as a reference for
        the manual pointer manipulation.

        Time complexity:  O(m * n)
        Space complexity: O(m * n)
        """
        cols: int = len(boxGrid[0])

        for r in range(len(boxGrid)):
            p: int = cols - 1
            c: int = cols - 1
            while p >= 0:
                if boxGrid[r][p] == '.':
                    p -= 1
                elif boxGrid[r][p] == '#':
                    boxGrid[r][p] = '.'
                    boxGrid[r][c] = '#'
                    c -= 1
                    p -= 1
                elif boxGrid[r][p] == '*':
                    p = p - 1
                    c = p

        return [list(row) for row in zip(*boxGrid[::-1])]


if __name__ == "__main__":
    test_cases: list[tuple[list[list[str]], list[list[str]]]] = [
        (
            [["#", ".", "#"]],
            [["."], ["#"], ["#"]],
        ),
        (
            [["#", ".", "*", "."],
             ["#", "#", "*", "."]],
            [["#", "."],
             ["#", "#"],
             ["*", "*"],
             [".", "."]],
        ),
        (
            [["#", "#", "*", ".", "*", "."],
             ["#", "#", "#", "*", ".", "."],
             ["#", "#", "#", ".", "#", "."]],
            [[".", "#", "#"],
             [".", "#", "#"],
             ["#", "#", "*"],
             ["#", "*", "."],
             ["#", ".", "*"],
             ["#", ".", "."]],
        ),
    ]

    solution = Solution()

    for label, method in [
        ("rotateTheBox     ", solution.rotateTheBox),
        ("rotateTheBoxWhile", solution.rotateTheBoxWhile),
    ]:
        for i, (grid, expected) in enumerate(test_cases, 1):
            g = copy.deepcopy(grid)
            result = method(g)
            assert result == expected, \
                f"{label} test {i} failed: expected {expected}, got {result}"
        print(f"  {label} passed")

    print("All test cases passed!")
