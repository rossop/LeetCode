"""
2540. Minimum Common Value

Given two integer arrays sorted in non-decreasing order, return the smallest
integer that appears in both. Return -1 if none.

Problem Link: https://leetcode.com/problems/minimum-common-value/

Examples:
    Example 1:
        Input: nums1 = [1, 2, 3], nums2 = [2, 4]
        Output: 2

    Example 2:
        Input: nums1 = [1, 2, 3, 6], nums2 = [2, 3, 4, 5]
        Output: 2

Constraints:
    1 <= nums1.length, nums2.length <= 10^5
    1 <= nums1[i], nums2[j] <= 10^9
    Both nums1 and nums2 are sorted in non-decreasing order.
"""


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Two pointers walking the sorted arrays in tandem. Advance whichever
        side is smaller; equal values are by definition the smallest common
        element seen so far (and the arrays are sorted), so return on the
        first match. Disjoint-range short-circuits skip the walk entirely.

        Time complexity:  O(n + m)
        Space complexity: O(1)
        """
        p1, p2 = 0, 0
        n1, n2 = len(nums1), len(nums2)

        if nums1[-1] < nums2[0]:
            return -1
        if nums2[-1] < nums1[0]:
            return -1

        while p1 < n1 and p2 < n2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                return nums1[p1]

        return -1

    def getCommonList(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Same two-pointer walk, but collect every common value then return
        its min. Strictly weaker than getCommon — the first match is already
        minimal — but useful as a sanity check.

        Time complexity:  O(n + m)
        Space complexity: O(k) — k = number of common values.
        """
        p1, p2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        common: list[int] = []
        while p1 < n1 and p2 < n2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                common.append(nums1[p1])
                p1 += 1
                p2 += 1

        if common:
            return min(common)
        return -1

    def getCommonSet(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Set-intersection variant — ignores the sorted-input gift. Quick to
        write, but O(n + m) extra space and a full materialization of the
        intersection before the min.

        Time complexity:  O(n + m)
        Space complexity: O(n + m)
        """
        common: set[int] = set(nums1).intersection(nums2)
        if common:
            return min(common)
        return -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3], [2, 4], 2),
        ([1, 2, 3, 6], [2, 3, 4, 5], 2),
        ([1, 2, 3], [4, 5, 6], -1),
        ([5], [5], 5),
        ([1, 1, 2], [2, 2, 3], 2),
    ]

    for i, (nums1, nums2, expected) in enumerate(test_cases, 1):
        assert solution.getCommon(list(nums1), list(nums2)) == expected, f"getCommon test {i} failed"
        assert solution.getCommonList(list(nums1), list(nums2)) == expected, f"getCommonList test {i} failed"
        assert solution.getCommonSet(list(nums1), list(nums2)) == expected, f"getCommonSet test {i} failed"

    print("All test cases passed!")
