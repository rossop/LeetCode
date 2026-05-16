"""
2784. Check if Array is Good

An array is "good" if it is a permutation of base[n] = [1, 2, ..., n - 1, n, n]
(length n + 1, contains each of 1..n-1 exactly once, plus two copies of n).

Problem Link: https://leetcode.com/problems/check-if-array-is-good/

Examples:
    Example 1:
        Input: nums = [2, 1, 3]
        Output: false

    Example 2:
        Input: nums = [1, 3, 3, 2]
        Output: true

    Example 3:
        Input: nums = [1, 1]
        Output: true

    Example 4:
        Input: nums = [3, 4, 4, 1, 2, 1]
        Output: false

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 200
"""


class Solution:
    def isGood(self, nums: list[int]) -> bool:
        """
        Mask-based single pass: n is forced to be max(nums); fill a length-n
        mask, rejecting any duplicate for values < n. Final check ensures the
        max appears exactly twice and every slot was hit (sum == n + 1).

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        n: int = max(nums)
        mask: list[int] = [0] * n

        for v in nums:
            if v < n:
                if mask[v - 1] == 0:
                    mask[v - 1] += 1
                else:
                    return False
            elif v == n:
                mask[v - 1] += 1

        return mask[-1] == 2 and sum(mask) == n + 1

    def isGoodSort(self, nums: list[int]) -> bool:
        """
        Sort then verify the shape directly: length must be max + 1, the last
        two entries must be equal, and the distinct-count must be length - 1.

        Time complexity:  O(n log n)
        Space complexity: O(n) — for the set used in the distinct check.
        """
        nums.sort()
        n: int = len(nums)
        return (
            n == nums[-1] + 1
            and nums[-1] == nums[-2]
            and n == len(set(nums)) + 1
        )


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 1, 3], False),
        ([1, 3, 3, 2], True),
        ([1, 1], True),
        ([3, 4, 4, 1, 2, 1], False),
        ([1, 2, 3, 4, 4], True),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.isGood(list(nums))
        result_sort = solution.isGoodSort(list(nums))
        assert result == expected, f"isGood test {i} failed: expected {expected}, got {result}"
        assert result_sort == expected, f"isGoodSort test {i} failed: expected {expected}, got {result_sort}"

    print("All test cases passed!")
