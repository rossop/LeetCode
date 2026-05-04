"""
48. Rotate Image

You are given an n x n 2D matrix representing an image. Rotate the image by
90 degrees clockwise. You must rotate the image in-place.

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

Examples:

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

import copy


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotates the matrix 90° clockwise in-place via transpose + reflect.

        Step 1 — Transpose: swap matrix[i][j] with matrix[j][i] for j > i.
          Turns rows into columns.
        Step 2 — Reflect horizontally: reverse each row.
          Mirrors columns left-to-right, completing the 90° turn.

        Time complexity:  O(n²)
        Space complexity: O(1) — in-place, no extra matrix
        """
        n: int = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

    def rotateLayerByLayer(self, matrix: list[list[int]]) -> None:
        """
        Rotates the matrix 90° clockwise in-place layer by layer.

        Processes concentric rings from outermost to innermost. Within each
        ring, every element is shifted one position clockwise in a four-way
        swap using a single saved value:

          top-left ← bottom-left ← bottom-right ← top-right ← top-left

        Pointers l and r mark the current ring's left and right boundaries;
        i offsets each of the ring's (r - l) column positions.

        Time complexity:  O(n²)
        Space complexity: O(1) — in-place, one temp variable per swap
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                top_left: int = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = top_left

            r -= 1
            l += 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        ),
        ([[1]], [[1]]),
    ]

    for label, method in [
        ("rotate          ", solution.rotate),
        ("rotateLayerByLayer", solution.rotateLayerByLayer),
    ]:
        for matrix, expected in test_cases:
            m = copy.deepcopy(matrix)
            method(m)
            assert m == expected, \
                f"{label} failed: got {m}, expected {expected}"
        print(f"  {label} passed")

    print("All test cases passed!")
