"""
1929. Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of
length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for
0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Problem Link: https://leetcode.com/problems/concatenation-of-array/

Examples:
    Example 1:
        Input: nums = [1,2,1]
        Output: [1,2,1,1,2,1]

    Example 2:
        Input: nums = [1,3,2,1]
        Output: [1,3,2,1,1,3,2,1]

Constraints:
    n == nums.length
    1 <= n <= 1000
    1 <= nums[i] <= 1000

This script contains a Solution class with two methods to solve the problem:
- `getConcatenation`: A method that manually creates a new array with double
  the length of the input and assigns values accordingly.
- `getConcatenationSimple`: A more concise method that leverages Python's
  list concatenation to achieve the same result.
"""

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        This method creates a new list `ans` of length 2n and assigns the
        elements of `nums` to the appropriate positions.

        Time Complexity: O(n) where n is the length of nums.
        Space Complexity: O(2n) since we're creating a new list twice the size
        of nums.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            List[int]: The concatenated list.
        """
        n: int = len(nums)
        ans: List[int] = [0] * 2 * n
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans

    def getConcatenationSimple(self, nums: List[int]) -> List[int]:
        """
        This method leverages Python's list concatenation to simply return
        `nums + nums`.

        Time Complexity: O(n) where n is the length of nums.
        Space Complexity: O(2n) since the concatenated list is twice the size
        of nums.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            List[int]: The concatenated list.
        """
        return nums + nums


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
        ([5], [5, 5]),
        ([9, 8, 7, 6], [9, 8, 7, 6, 9, 8, 7, 6])
    ]

    for numbers, expected in test_cases:
        result = solution.getConcatenation(numbers)
        assert result == expected, f"""
        Test case failed: expected {expected}, got {result}
        """

        result_simple = solution.getConcatenationSimple(numbers)
        assert result_simple == expected, f"""
        Test case failed: expected {expected}, got {result_simple}
        """

    print("All test cases passed!")
