"""
1855. Maximum Distance Between a Pair of Values

Problem Statement:
You are given two non-increasing 0-indexed integer arrays nums1 and nums2.
A pair of indices (i, j) is valid if i <= j and nums1[i] <= nums2[j].
The distance of the pair is j - i.

Return the maximum distance of any valid pair (i, j), or 0 if none exist.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 1 <= nums1[i], nums2[j] <= 10^5
- Both nums1 and nums2 are non-increasing.

Examples:

Example 1:
    Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
    Output: 2
    Explanation: Maximum distance is 2 with pair (2,4).

Example 2:
    Input: nums1 = [2,2,2], nums2 = [10,10,1]
    Output: 1
    Explanation: Maximum distance is 1 with pair (0,1).

Example 3:
    Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
    Output: 2
    Explanation: Maximum distance is 2 with pair (2,4).
"""

from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Returns the maximum distance j - i over all valid pairs using two pointers.

        Both arrays are non-increasing, so the condition nums1[i] <= nums2[j]
        can only hold for larger j (further right in nums2) or smaller i (further
        left in nums1). This gives a greedy two-pointer strategy:
        - If nums1[i] <= nums2[j]: valid pair found, record distance, advance j
          to try for a larger distance.
        - If nums1[i] > nums2[j]: this i has no valid j at this position or earlier;
          advance i to try a smaller nums1 value.

        When i temporarily exceeds j the distance j - i is negative; max() with
        the running best ensures these non-valid positions are ignored.

        Args:
            nums1 (List[int]): Non-increasing array.
            nums2 (List[int]): Non-increasing array.

        Returns:
            int: Maximum valid pair distance, or 0 if no valid pair exists.

        Time complexity:  O(n + m) — each pointer advances at most len(nums1) +
                          len(nums2) steps combined.
        Space complexity: O(1)
        """
        i, j = 0, 0
        max_dist: int = 0
        len1, len2 = len(nums1), len(nums2)

        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1
        return max_dist

    def maxDistanceNaive(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Returns the maximum distance j - i over all valid pairs using brute force.

        For each i, scans j from i onwards. Breaks early when nums2[j] drops
        below nums1[i] (exploiting the non-increasing property of nums2), so
        it avoids checking all n² pairs in practice — but worst case remains O(n²).

        Args:
            nums1 (List[int]): Non-increasing array.
            nums2 (List[int]): Non-increasing array.

        Returns:
            int: Maximum valid pair distance, or 0 if no valid pair exists.

        Time complexity:  O(n × m) worst case.
        Space complexity: O(1)
        """
        max_dist: int = 0
        len1, len2 = len(nums1), len(nums2)

        for i in range(len1):
            for j in range(i, len2):
                if nums1[i] <= nums2[j]:
                    max_dist = max(max_dist, j - i)
                else:
                    break

        return max_dist


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([55, 30, 5, 4, 2], [100, 20, 10, 10, 5], 2),
        ([2, 2, 2],          [10, 10, 1],          1),
        ([30, 29, 19, 5],    [25, 25, 25, 25, 25], 2),
        ([5],                [5],                  0),
        ([1],                [1],                  0),
    ]

    for label, method in [
        ("maxDistance     ", solution.maxDistance),
        ("maxDistanceNaive", solution.maxDistanceNaive),
    ]:
        for nums1, nums2, expected in test_cases:
            result = method(nums1, nums2)
            assert result == expected, \
                f"{label} failed on nums1={nums1}, nums2={nums2}: expected {expected}, got {result}"
        print(f"  {label} passed")

    print("All test cases passed!")
