"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: Merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: Merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from typing import List


class Solution:
    def findMedianSortedArraysMerge(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Merge-based approach to find the median of two sorted arrays.
        This approach has a time complexity of O(m + n).

        Args:
            nums1 (List[int]): The first sorted array.
            nums2 (List[int]): The second sorted array.

        Returns:
            float: The median of the two sorted arrays.
        """
        p1: int = 0
        p2: int = 0
        n1: int = len(nums1)
        n2: int = len(nums2)
        m: int = n1 + n2
        nums: List[int] = []

        # Merge lists using two pointers
        while p1 < n1 and p2 < n2:
            if nums1[p1] < nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1

        # Append remaining elements from nums1
        while p1 < n1:
            nums.append(nums1[p1])
            p1 += 1

        # Append remaining elements from nums2
        while p2 < n2:
            nums.append(nums2[p2])
            p2 += 1

        # Find median of merged array
        if m % 2 == 0:
            return (nums[m//2 - 1] + nums[m//2]) / 2
        return nums[m//2]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary search approach to find the median of two sorted arrays.
        This approach has a time complexity of O(log(min(m, n))).

        Args:
            nums1 (List[int]): The first sorted array.
            nums2 (List[int]): The second sorted array.

        Returns:
            float: The median of the two sorted arrays.
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0)
    ]

    for nums1, nums2, expected in test_cases:
        result_merge = solution.findMedianSortedArraysMerge(nums1, nums2)
        result_binary = solution.findMedianSortedArrays(nums1, nums2)
        assert result_merge == expected, f"Merge-based method failed for {nums1}, {nums2}. Expected {expected}, got {result_merge}"
        assert result_binary == expected, f"Binary search method failed for {nums1}, {nums2}. Expected {expected}, got {result_binary}"

    print("All test cases passed!")
