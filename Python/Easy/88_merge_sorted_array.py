from typing import List

class Solution:
    """
    A class to solve the 'Merge Sorted Array' problem.

    Problem:
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
        and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.

        The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
        To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
        and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

    Example 1:
        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
        The result of the merge is [1,2,2,3,5,6].

    Example 2:
        Input: nums1 = [1], m = 1, nums2 = [], n = 0
        Output: [1]
        Explanation: The arrays we are merging are [1] and [].
        The result of the merge is [1].

    Example 3:
        Input: nums1 = [0], m = 0, nums2 = [1], n = 1
        Output: [1]
        Explanation: The arrays we are merging are [] and [1].
        The result of the merge is [1].

    Constraints:
        - nums1.length == m + n
        - nums2.length == n
        - 0 <= m, n <= 200
        - 1 <= m + n <= 200
        - -10^9 <= nums1[i], nums2[j] <= 10^9

    Follow-up:
        Can you come up with an algorithm that runs in O(m + n) time?
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 in-place, assuming nums1 has enough space at the end to accommodate nums2.
        The first m elements of nums1 contain valid data, and nums2 contains n elements.
        The final sorted result should be stored in nums1.

        Args:
            nums1 (List[int]): The first sorted array with length m + n, where the first m elements
                               represent the elements to be merged, and the remaining n elements are 0s.
            m (int): The number of elements in nums1 to be merged.
            nums2 (List[int]): The second sorted array with length n.
            n (int): The number of elements in nums2.

        Returns:
            None: The result is stored in-place in nums1.
        """
        # Initialize three pointers
        p = m + n - 1  # Pointer for the last position in nums1
        p1 = m - 1     # Pointer for the last element in the initial part of nums1
        p2 = n - 1     # Pointer for the last element in nums2

        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy remaining elements from nums2, if any
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

if __name__ == "__main__":
    # Test cases with expected outcomes
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ([2, 0], 1, [1], 1, [1, 2])
    ]

    solution = Solution()

    for i, (nums1, m, nums2, n, expected) in enumerate(test_cases, 1):
        solution.merge(nums1, m, nums2, n)
        assert nums1 == expected, f"Test case {i} failed: expected {expected}, got {nums1}"
        print(f"Test case {i} passed: {nums1}")

    print("All test cases passed!")