"""
153. Find Minimum in Rotated Sorted Array

A sorted array of unique elements has been rotated between 1 and n times.
Return the minimum element in O(log n).

Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Examples:
    Example 1:
        Input: nums = [3, 4, 5, 1, 2]
        Output: 1

    Example 2:
        Input: nums = [4, 5, 6, 7, 0, 1, 2]
        Output: 0

    Example 3:
        Input: nums = [11, 13, 15, 17]
        Output: 11

Constraints:
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All integers are unique.
    nums is sorted and rotated between 1 and n times.
"""

from bisect import bisect_left


class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Binary search on the pivot. Compare the midpoint with the right end:
        if mid > right, the minimum lies strictly to the right of mid; else it
        is at mid or to its left. Loop until l == r — that index is the min.

        Time complexity:  O(log n)
        Space complexity: O(1)
        """
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]

    def findMinBisect(self, nums: list[int]) -> int:
        """
        Reframe the rotated array as a boolean predicate (n <= nums[-1]):
        False on the pre-rotation prefix, True on the suffix containing the
        minimum. bisect_left finds the first True — the rotation point.

        Time complexity:  O(log n)
        Space complexity: O(1)
        """
        return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([1], 1),
        ([2, 1], 1),
        ([5, 1, 2, 3, 4], 1),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.findMin(list(nums))
        result_bisect = solution.findMinBisect(list(nums))
        assert result == expected, f"findMin test {i} failed: expected {expected}, got {result}"
        assert result_bisect == expected, f"findMinBisect test {i} failed: expected {expected}, got {result_bisect}"

    print("All test cases passed!")
