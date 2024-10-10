"""
962. Maximum Width Ramp

Problem Statement:
A ramp in an integer array `nums` is a pair (i, j) for which i < j and nums[i] <= nums[j].
The width of such a ramp is `j - i`.

Given an integer array `nums`, return the maximum width of a ramp in `nums`.
If there is no ramp in `nums`, return 0.

Constraints:
- 2 <= nums.length <= 5 * 10^4
- 0 <= nums[i] <= 5 * 10^4

Examples:

Example 1:
    Input: nums = [6, 0, 8, 2, 1, 5]
    Output: 4
    Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

Example 2:
    Input: nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
    Output: 7
    Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
"""

from typing import List, Optional

class Solution:
    """
    This class implements multiple methods to calculate the maximum width ramp in an integer array.
    
    Methods:
    1. maxWidthRamp: A placeholder for future improvements.
    2. maxWidthRampTwoPointers: Uses a two-pointer approach to find the maximum width ramp.
    3. maxWidthRampSorting: Uses sorting of indices to compute the maximum width ramp.
    4. maxWidthRampBruteForce: Uses a brute-force approach to find the maximum width ramp.
    """

    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        A placeholder method for future optimized approaches.
        """
        pass

    def maxWidthRampTwoPointers(self, nums: List[int]) -> int:
        """
        Uses two pointers and a precomputed right maximum array to find the maximum width ramp.
        
        Time Complexity: O(n), where n is the length of the array `nums`.
        Space Complexity: O(n), due to the space needed for the `right_max` array.

        Args:
            nums: List[int] - The input list of integers.

        Returns:
            int - The maximum width of the ramp found in the array.
        """
        n: int = len(nums)
        right_max: List[Optional[int]] = [None] * n

        # Fill right_max array with the maximum values from the right
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        left: int = 0
        right: int = 0
        max_width: int = 0

        # Two-pointer approach to find the maximum width ramp
        while right < n:
            while left < right and nums[left] > right_max[right]:
                left += 1
            max_width = max(max_width, right - left)
            right += 1

        return max_width

    def maxWidthRampSorting(self, nums: List[int]) -> int:
        """
        Sorts the indices based on the values in `nums` and finds the maximum width ramp.
        
        Time Complexity: O(n log n), due to sorting.
        Space Complexity: O(n), for storing the sorted indices.

        Args:
            nums: List[int] - The input list of integers.

        Returns:
            int - The maximum width of the ramp found in the array.
        """
        n: int = len(nums)
        indices: List[int] = [i for i in range(n)]

        # Sort indices by the values in `nums` and by the indices to preserve order
        indices.sort(key=lambda i: (nums[i], i))

        min_index: int = n
        max_width: int = 0

        # Traverse the sorted indices and calculate the maximum width
        for i in indices:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)

        return max_width

    def maxWidthRampBruteForce(self, nums: List[int]) -> int:
        """
        Brute-force approach to find the maximum width ramp.
        
        Time Complexity: O(n^2), due to checking all possible pairs.
        Space Complexity: O(1).

        Args:
            nums: List[int] - The input list of integers.

        Returns:
            int - The maximum width of the ramp found in the array.
        """
        n: int = len(nums)
        max_width: int = 0

        # Check all pairs (i, j) and find the maximum width ramp
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] <= nums[j]:
                    max_width = max(max_width, j - i)
        return max_width


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ([6, 0, 8, 2, 1, 5], 4),    # Expected output is 4 (ramp from index 1 to 5)
        ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7),  # Expected output is 7 (ramp from index 2 to 9)
        ([1, 2, 3, 4, 5], 4),       # Entire array forms the ramp, width is 4
        ([5, 4, 3, 2, 1], 0),       # No valid ramp, output is 0
    ]

    solution = Solution()

    # Test the brute-force method
    print("Testing maxWidthRampBruteForce method:")
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.maxWidthRampBruteForce(nums)
        assert result == expected, f"Test case {i+1} failed (Brute-force): Expected {expected}, but got {result}"
    print("All test cases passed for maxWidthRampBruteForce method!")

    # Test the sorting-based method
    print("\nTesting maxWidthRampSorting method:")
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.maxWidthRampSorting(nums)
        assert result == expected, f"Test case {i+1} failed (Sorting): Expected {expected}, but got {result}"
    print("All test cases passed for maxWidthRampSorting method!")

    # Test the two-pointer method
    print("\nTesting maxWidthRampTwoPointers method:")
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.maxWidthRampTwoPointers(nums)
        assert result == expected, f"Test case {i+1} failed (Two-pointers): Expected {expected}, but got {result}"
    print("All test cases passed for maxWidthRampTwoPointers method!")