"""
1365. How Many Numbers Are Smaller Than the Current Number

For each nums[i], count how many j != i satisfy nums[j] < nums[i]. Return the
counts as an array, same order as the input.

Problem Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Examples:
    Example 1:
        Input: nums = [8, 1, 2, 2, 3]
        Output: [4, 0, 1, 1, 3]

    Example 2:
        Input: nums = [6, 5, 4, 8]
        Output: [2, 1, 0, 3]

    Example 3:
        Input: nums = [7, 7, 7, 7]
        Output: [0, 0, 0, 0]

Constraints:
    2 <= nums.length <= 500
    0 <= nums[i] <= 100
"""

from bisect import bisect_left


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        """
        Counting sort + prefix sum. Bucket every value in [0, 100], then the
        prefix at index v - 1 gives the count of values strictly less than v.
        Independent of n once the histogram is built.

        Time complexity:  O(n + k), k = value range (101).
        Space complexity: O(k)
        """
        all_nums: list[int] = [0] * 101
        res: list[int] = [0] * len(nums)

        for v in nums:
            all_nums[v] += 1

        for v in range(1, 101):
            all_nums[v] += all_nums[v - 1]

        for i, v in enumerate(nums):
            res[i] = 0 if v == 0 else all_nums[v - 1]
        return res

    def smallerNumbersThanCurrentSort(self, nums: list[int]) -> list[int]:
        """
        Sort a copy; for each original value, the index of its first
        occurrence in the sorted array equals the count of strictly-smaller
        values. bisect_left finds that index in O(log n).

        Time complexity:  O(n log n)
        Space complexity: O(n) — for the sorted copy.
        """
        sorted_nums: list[int] = sorted(nums)
        return [bisect_left(sorted_nums, v) for v in nums]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8], [2, 1, 0, 3]),
        ([7, 7, 7, 7], [0, 0, 0, 0]),
        ([0, 0, 1], [0, 0, 2]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.smallerNumbersThanCurrent(list(nums)) == expected, f"prefix-sum test {i} failed"
        assert solution.smallerNumbersThanCurrentSort(list(nums)) == expected, f"sort test {i} failed"

    print("All test cases passed!")
