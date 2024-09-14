"""
35. Search Insert Position

Problem Statement:
Given a sorted array of distinct integers and a target value, return the index 
if the target is found. If not, return the index where it would be if it were 
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1, 3, 5, 6], target = 5
    Output: 2

Example 2:
    Input: nums = [1, 3, 5, 6], target = 2
    Output: 1

Example 3:
    Input: nums = [1, 3, 5, 6], target = 7
    Output: 4

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Naive linear search solution to find the insertion point or the target.

        Time Complexity: O(n) where n is the number of elements in the list.
        Space Complexity: O(1) as we are not using any extra space.
        """
        n = len(nums)
        left: int = 0
        
        # Iterate over the array and find the right position for target
        while left < n:
            if nums[left] >= target:
                return left
            left += 1
        return left

    def searchInsertOptimized(self, nums: List[int], target: int) -> int:
        """
        Optimized solution using binary search to find the insertion point or the target.

        Time Complexity: O(log n) where n is the number of elements in the list.
        Space Complexity: O(1) as we are not using any extra space.
        """
        left: int = 0
        right: int = len(nums) - 1
        
        while left <= right:
            mid: int = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # When the loop ends, left is the insertion point
        return left


if __name__ == "__main__":
    # Example test cases
    solution = Solution()

    # Test cases with expected output
    test_cases = [
        ([1, 3, 5, 6], 5, 2),   # Example 1
        ([1, 3, 5, 6], 2, 1),   # Example 2
        ([1, 3, 5, 6], 7, 4),   # Example 3
        ([1, 3, 5, 6], 0, 0),   # Insert at the start
        ([1, 2, 4, 6, 7], 3, 2) # Insert in the middle
    ]

    # Run both methods for each test case
    for i, (nums, target, expected) in enumerate(test_cases):
        result = solution.searchInsert(nums.copy(), target)
        assert result == expected, f"Test case {i + 1} failed for searchInsert. Expected {expected}, got {result}."

        result_optimized = solution.searchInsertOptimized(nums.copy(), target)
        assert result_optimized == expected, f"Test case {i + 1} failed for searchInsertOptimized. Expected {expected}, got {result_optimized}."

        print(f"Test case {i + 1} passed for both methods!")

    print("All test cases passed!")
