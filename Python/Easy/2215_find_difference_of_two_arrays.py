"""
2215. Find the Difference of Two Arrays

Problem Statement: Given two 0-indexed integer arrays nums1 and nums2, return a
list answer of size 2 where: - answer[0] is a list of all distinct integers in
nums1 which are not present in nums2. - answer[1] is a list of all distinct
integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.

Example 1:
    Input: nums1 = [1,2,3], nums2 = [2,4,6] Output: [[1,3],[4,6]] Explanation: -
    For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1
    and nums1[2] = 3
      are not present in nums2. Therefore, answer[0] = [1,3].
    - For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] =
      4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].

Example 2:
    Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
    Output: [[3],[]]
    Explanation: - For nums1, nums1[2] and nums1[3] are not present in nums2.
    Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
    Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
      present in nums1. Therefore, answer[1] = [].

Constraints:
    - 1 <= nums1.length, nums2.length <= 1000
    - -1000 <= nums1[i], nums2[i] <= 1000
"""

from typing import List


class Solution:
    """
    A solution class for solving the problem of finding the difference of two
    arrays.
    """
    
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Finds the distinct elements in nums1 not present in nums2 and vice
        versa.

        Time Complexity: O(n + m) where n is the length of nums1 and m is the
        length of nums2. We are using set operations which take O(n) time for
        set(nums1) and O(m) for set(nums2).

        Space Complexity: O(n + m) where n and m are the sizes of nums1 and
        nums2. This is the space required to store the sets and results.

        Args:
            nums1: List of integers representing the first array.
            nums2: List of integers representing the second array.

        Returns:
            A list of two lists: - First list contains distinct integers from
            nums1 not in nums2. - Second list contains distinct integers from
            nums2 not in nums1.
        """
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


if __name__ == "__main__":
    # Example test cases
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    expected_output = [[1, 3], [4, 6]]
    assert solution.findDifference(nums1, nums2) == expected_output

    # Test case 2
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    expected_output = [[3], []]
    assert solution.findDifference(nums1, nums2) == expected_output

    # Test case 3: Custom test case
    nums1 = [10, 15, 20]
    nums2 = [15, 25, 30]
    expected_output = [[10, 20], [25, 30]]
    assert solution.findDifference(nums1, nums2) == expected_output

    print("All test cases passed!")
