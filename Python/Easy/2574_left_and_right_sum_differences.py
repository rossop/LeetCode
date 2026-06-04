"""
2574. Left and Right Sum Differences

You are given a 0-indexed integer array nums of size n. Define two arrays
leftSum and rightSum where leftSum[i] is the sum of elements strictly to the
left of index i (0 if none) and rightSum[i] is the sum strictly to the right
(0 if none). Return answer where answer[i] = |leftSum[i] - rightSum[i]|.

Problem Link: https://leetcode.com/problems/left-and-right-sum-differences/

Examples:
    Example 1:
        Input: nums = [10, 4, 8, 3]
        Output: [15, 1, 11, 22]
        Explanation:
            leftSum  = [0, 10, 14, 22]
            rightSum = [15, 11, 3, 0]
            answer   = [15, 1, 11, 22]

    Example 2:
        Input: nums = [1]
        Output: [0]

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 10^5
"""


class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        """
        Single pass with running counters. Pre-compute right = sum(nums),
        then walk left to right: subtract the current element from right
        (it is no longer "to the right"), record |right - left|, and add
        the element to left (it becomes "to the left" for the next index).

        Time complexity:  O(n)
        Space complexity: O(1) auxiliary (output excluded).
        """
        ans: list[int] = []
        left: int = 0
        right: int = sum(nums)

        for n in nums:
            right -= n
            ans.append(abs(right - left))
            left += n

        return ans

    def leftRightDifferenceTwoPass(self, nums: list[int]) -> list[int]:
        """
        Two-pass approach that reuses the answer array as scratch:
        first pass writes leftSum[i] into ans[i]; second pass walks
        right to left and rewrites each cell to |ans[i] - rightSum|.

        Time complexity:  O(n)
        Space complexity: O(1) auxiliary (output excluded).
        """
        n: int = len(nums)
        ans: list[int] = [0] * n

        left_sum: int = 0
        for i in range(n):
            ans[i] = left_sum
            left_sum += nums[i]

        right_sum: int = 0
        for i in range(n - 1, -1, -1):
            ans[i] = abs(ans[i] - right_sum)
            right_sum += nums[i]

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([10, 4, 8, 3], [15, 1, 11, 22]),
        ([1], [0]),
        ([1, 2, 3, 4, 5], [14, 11, 6, 1, 10]),
        ([5, 5], [5, 5]),
        ([0, 0, 0], [0, 0, 0]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.leftRightDifference(list(nums)) == expected, f"single-pass test {i} failed: {nums}"
        assert solution.leftRightDifferenceTwoPass(list(nums)) == expected, f"two-pass test {i} failed: {nums}"

    print("All test cases passed!")
