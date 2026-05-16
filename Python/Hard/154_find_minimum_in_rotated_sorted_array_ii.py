"""
154. Find Minimum in Rotated Sorted Array II

A sorted array (possibly with duplicates) has been rotated between 1 and n
times. Return the minimum element, minimizing operation steps.

Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Examples:
    Example 1:
        Input: nums = [1, 3, 5]
        Output: 1

    Example 2:
        Input: nums = [2, 2, 2, 0, 1]
        Output: 0

Constraints:
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    nums is sorted and rotated between 1 and n times.
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Binary search against the right end. nums[m] > nums[r] forces the min
        strictly right of m; nums[m] < nums[r] keeps the min at or before m;
        equality is ambiguous (duplicates), so safely shrink r by one — we
        still own a copy of nums[r] at index m.

        Time complexity:  O(log n) average, O(n) worst case (all equal).
        Space complexity: O(1)
        """
        l, r = 0, len(nums) - 1

        while l < r:
            m: int = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1

        return nums[l]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 3, 5], 1),
        ([2, 2, 2, 0, 1], 0),
        ([3, 1, 3], 1),
        ([1, 1, 1, 1], 1),
        ([10, 1, 10, 10, 10], 1),
        ([1], 1),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.findMin(list(nums))
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")
