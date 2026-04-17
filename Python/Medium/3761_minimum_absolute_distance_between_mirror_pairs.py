"""
3761. Minimum Absolute Distance Between Mirror Pairs

Problem Statement:
You are given an integer array nums.

A mirror pair is a pair of indices (i, j) such that:
    0 <= i < j < nums.length, and
    reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed
    by reversing the digits of x. Leading zeros are omitted after reversing,
    e.g. reverse(120) = 21.

Return the minimum absolute distance between the indices of any mirror pair.
If no mirror pair exists, return -1.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9

Examples:

Example 1:
    Input: nums = [12,21,45,33,54]
    Output: 1
    Explanation: Mirror pairs are (0,1) with distance 1 and (2,4) with distance 2.

Example 2:
    Input: nums = [120,21]
    Output: 1
    Explanation: reverse(120) = 21, so (0,1) is a mirror pair with distance 1.

Example 3:
    Input: nums = [21,120]
    Output: -1
    Explanation: No mirror pairs exist.
"""
from bisect import bisect_right


class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        """
        Returns the minimum absolute index distance between any mirror pair in nums,
        or -1 if no mirror pair exists.

        Single pass using a hash map that tracks the most recent index for each
        reversed value. For each index i with value v, checks if v exists as a key
        (meaning a previous j stored reverse(nums[j]) = v there), giving a valid
        pair (j, i). Then stores reverse(v) → i for future lookups.

        Because the most recent j always gives the smallest distance for a given i,
        only one index per key is needed — no binary search required.

        Args:
            nums (list[int]): The input array of integers.

        Returns:
            int: The minimum abs(i - j) across all mirror pairs, or -1 if none exist.

        Time Complexity:
            O(n): Single pass with O(1) hash map operations.

        Space Complexity:
            O(n): The hash map stores at most one index per unique reversed value.

        # TODO: Review
        """
        def reverse(num: int) -> int:
            return int(str(num)[::-1])

        last_seen: dict[int, int] = {}
        ans = float('inf')

        for i, v in enumerate(nums):
            if v in last_seen:
                j = last_seen[v]
                dist: int = i - j
                ans = min(ans, dist)
            last_seen[reverse(v)] = i

        return ans if ans != float('inf') else -1


    def minMirrorPairDistanceBisect(self, nums: list[int]) -> int:
        """
        Returns the minimum absolute index distance between any mirror pair in nums,
        or -1 if no mirror pair exists.

        Builds a value-to-sorted-indices map in one pass, then for each index i
        uses binary search to find the closest j > i where nums[j] == reverse(nums[i]).
        Only j > i is valid since the mirror pair definition requires i < j and
        reverse(nums[i]) == nums[j] — the relationship is not symmetric when trailing
        zeros are involved (e.g. reverse(120)=21 but reverse(21)=12 ≠ 120).

        Args:
            nums (list[int]): The input array of integers.

        Returns:
            int: The minimum abs(i - j) across all mirror pairs, or -1 if none exist.

        Time Complexity:
            O(n log n): One O(n) pass to build the map, then O(log n) per element
            for binary search.

        Space Complexity:
            O(n): The positions map stores all indices.
        """
        def reverse(num: int) -> int:
            return int(str(num)[::-1])

        # Pass 1: build a plain value → sorted indices map
        positions: dict[int, list[int]] = {}
        for i, num in enumerate(nums):
            positions.setdefault(num, []).append(i)

        # Pass 2: for each index i, find the closest j > i where nums[j] == reverse(nums[i])
        ans = float('inf')
        for i, num in enumerate(nums):
            rev: int = reverse(num)
            if rev not in positions:
                continue
            candidates = positions[rev]
            j: int = bisect_right(candidates, i)
            if j < len(candidates):
                ans = min(ans, candidates[j] - i)

        return ans if ans != float('inf') else -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([12, 21, 45, 33, 54], 1),
        ([120, 21], 1),
        ([21, 120], -1),
    ]

    for label, method in [
        ("O(n)     ", solution.minMirrorPairDistance),
        ("O(n logn)", solution.minMirrorPairDistanceBisect),
    ]:
        print(f"--- {label} ---")
        for i, (nums, expected) in enumerate(test_cases, 1):
            result = method(nums)
            assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
            print(f"  Test case {i} passed")

    print("All test cases passed!")
