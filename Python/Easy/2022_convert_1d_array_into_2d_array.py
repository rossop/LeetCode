"""
This Python file provides a solution to the LeetCode problem:

2022. Convert 1D Array Into 2D Array

You are given a 0-indexed 1-dimensional (1D) integer array `original`, and two
integers `m` and `n`. You are tasked with creating a 2-dimensional (2D) array
with `m` rows and `n` columns using all the elements from `original`.

The elements from indices 0 to n - 1 (inclusive) of `original` should form the
first row of the constructed 2D array, the elements from indices n to 2 * n - 1
(inclusive) should form the second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above procedure, or an
empty 2D array if it is impossible.

Example 1:
    Input: original = [1,2,3,4], m = 2, n = 2 Output: [[1,2],[3,4]]

Example 2:
    Input: original = [1,2,3], m = 1, n = 3 Output: [[1,2,3]]

Example 3:
    Input: original = [1,2], m = 1, n = 1 Output: [] Explanation: There are 2
    elements in original. It is impossible to fit 2 elements in a 1x1 2D array,
    so return an empty 2D array.

Constraints:
    - The length of the original array is in the range [1, 10^5].
    - m and n are positive integers.
"""

from typing import List


class Solution:
    """
    Provides a method to convert a 1D array into a 2D array if possible.
    """

    def construct2DArray(self,
                         original: List[int],
                         m: int, n: int) -> List[List[int]]:
        """
        Converts a 1D array into a 2D array with `m` rows and `n` columns.

        Args:
            original (List[int]): The 1D array to convert. m (int): The number
            of rows for the 2D array. n (int): The number of columns for the 2D
            array.

        Returns:
            List[List[int]]: The resulting 2D array, or an empty list if the
            conversion is not possible.

        Time Complexity: O(m*n) where m is the number of rows and n is the
        number of columns. Space Complexity: O(m*n) for the output 2D array.
        """
        if m * n != len(original):
            return []

        ans: List[List[int]] = []
        for i in range(m):
            row: List[int] = []
            for j in range(n):
                row.append(original[i * n + j])
            ans.append(row)
        return ans


if __name__ == "__main__":
    # Test cases for construct2DArray
    test_cases = [
        ([1, 2, 3, 4], 2, 2, [[1, 2], [3, 4]]),  # Example 1
        ([1, 2, 3], 1, 3, [[1, 2, 3]]),          # Example 2
        ([1, 2], 1, 1, []),                      # Example 3 (not possible to fit)
        ([1, 2, 3, 4, 5, 6], 2, 3, [[1, 2, 3], [4, 5, 6]]),  # Additional test case 1
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, 2, [[1, 2], [3, 4], [5, 6], [7, 8]]),  # Additional test case 2
    ]

    solution = Solution()

    for k, (original, m, n, expected) in enumerate(test_cases):
        result = solution.construct2DArray(original, m, n)
        assert result == expected, f"construct2DArray test case {k+1} failed: Expected {expected}, but got {result}"

    print("All test cases passed!")
