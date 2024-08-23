"""
1920. Build Array from Permutation

Given a zero-based permutation nums (0-indexed), build an array ans of the
same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and
return it.

A zero-based permutation nums is an array of distinct integers from
0 to nums.length - 1 (inclusive).

Problem Link: https://leetcode.com/problems/build-array-from-permutation/

Examples:
    Example 1:
        Input: nums = [0,2,1,5,3,4]
        Output: [0,1,2,4,5,3]

    Example 2:
        Input: nums = [5,0,1,2,3,4]
        Output: [4,5,0,1,2,3]

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] < nums.length
    The elements in nums are distinct.
"""

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Build an array `ans` where `ans[i] = nums[nums[i]]` using a new list
        for storing the result.

        Time Complexity: O(n), where n is the length of the input list nums.
        Space Complexity: O(n) due to the extra space used by the `ans` list.

        Args:
            nums (List[int]): The input list of integers representing a
            zero-based permutation.

        Returns:
            List[int]: The list generated from the permutation.
        """
        n: int = len(nums)
        ans: List[int] = [0] * n

        for i in range(n):
            ans[i] = nums[nums[i]]

        return ans

    def buildArrayInPlace(self, nums: List[int]) -> List[int]:
        """
        Build an array `ans` where `ans[i] = nums[nums[i]]` without using
        extra space. This method leverages the properties of modular arithmetic
        to store both the old and new values in the same array.

        Time Complexity: O(n), where n is the length of the input list nums.
        Space Complexity: O(1), since no extra space is used except for the
        input list.

        Args:
            nums (List[int]): The input list of integers representing a
            zero-based permutation.

        Returns:
            List[int]: The list generated from the permutation.
        """
        n: int = len(nums)

        for i in range(n):
            nums[i] = nums[i] + (nums[nums[i]] % n) * n

        for i in range(n):
            nums[i] = nums[i] // n

        return nums


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3]),
        ([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3]),
        ([0], [0]),
        ([4, 3, 2, 1, 0], [0, 1, 2, 3, 4])
    ]

    for numbers, expected in test_cases:
        # Test the basic method
        result = solution.buildArray(numbers.copy())
        assert result == expected, f"""
            Test case failed: expected {expected}, got {result}
            """

        # Test the in-place method
        result_in_place = solution.buildArrayInPlace(numbers.copy())
        assert result_in_place == expected, f"""
            Test case failed: expected {expected}, got {result_in_place}
            """

    print("All test cases passed!")
