"""
1848. Minimum Distance to the Target Element

Problem Statement:
Given a 0-indexed integer array `nums` and two integers `target` and `start`,
find an index `i` such that `nums[i] == target` and `abs(i - start)` is minimized.
Return the minimum value of `abs(i - start)`.

It is guaranteed that `target` exists in `nums`.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
- 0 <= start < nums.length
- target is in nums

Examples:

Example 1:
    Input: nums = [1,2,3,4,5], target = 5, start = 3
    Output: 1
    Explanation: nums[4] = 5 is the only value equal to target. abs(4 - 3) = 1.

Example 2:
    Input: nums = [1], target = 1, start = 0
    Output: 0
    Explanation: nums[0] = 1 is the only value equal to target. abs(0 - 0) = 0.

Example 3:
    Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
    Output: 0
    Explanation: Every value in nums is equal to target, so abs(0 - 0) = 0 is the minimum.
"""

from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        """
        Finds the minimum absolute distance between start and any index where nums[i] == target.

        Iterates through the array, tracking the minimum of abs(i - start) for all
        indices where the value equals target.

        Args:
            nums (List[int]): The input array of integers.
            target (int): The target value to find in nums.
            start (int): The starting index to measure distance from.

        Returns:
            int: The minimum absolute distance to any occurrence of target.

        Time Complexity:
            O(n): Single pass through the array.

        Space Complexity:
            O(1): No extra space used.
        """
        res: int = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                res = min(res, abs(i - start))
        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5], 5, 3, 1),
        ([1], 1, 0, 0),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0, 0),
    ]

    for i, (nums, target, start, expected) in enumerate(test_cases, 1):
        result = solution.getMinDistance(nums, target, start)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed")

    print("All test cases passed!")
