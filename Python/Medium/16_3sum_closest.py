"""
16. 3Sum Closest

Problem Statement: Given an integer array nums of length n and an integer
target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
    Input: nums = [-1,2,1,-4], target = 1 Output: 2 Explanation: The sum that's
    closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
    Input: nums = [0,0,0], target = 1 Output: 0 Explanation: The sum that is
    closest to the target is 0. (0 + 0 + 0 = 0).

Constraints: - 3 <= nums.length <= 500 - -1000 <= nums[i] <= 1000 - -10^4 <=
target <= 10^4

Approach: - Sort the array first. - Iterate over each element in the array, and
use two pointers (left and right)to find the sum of three numbers.
- If the current sum is closer to the target than the previously recorded
    closest sum, update the closest sum.
- Continue moving the pointers based on the comparison between the current sum
    and target.

Time Complexity: O(n^2), where n is the number of elements in the input array.
                 The outer loop runs n times, and for each iteration, the inner
                 while loop runs n times.
Space Complexity: O(1), since the algorithm uses constant extra space.
"""


class Solution:
    """
    Solution to the 3Sum Closest problem.
    """
    def threeSumClosest(self, nums, target):
        """
        Solves the 3Sum Closest problem by iterating over the array with fixed
        element and using two pointers to find the sum of three elements that
        is closest to the target.

        Args:
            nums: The input array of integers. target: The target sum that we
            want to get close to.

        Returns:
            The sum of the three integers closest to the target.
        """
        # Sort the array first
        nums.sort()
        n = len(nums)
        closest_sum = sum(nums[:3])  # Initialize closestSum

        # Iterate over each element to fix the first element of the triplet
        for p in range(n - 2):
            left = p + 1
            right = n - 1

            # While loop to process the two-pointer approach
            while left < right:
                curr_sum = nums[p] + nums[left] + nums[right]

                # If we find an exact match, return immediately
                if curr_sum == target:
                    return curr_sum

                # Update closestSum if the current sum is closer to the target
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                # Move pointers based on how currSum compares to the target
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum

    def threeSumClosestOptimized(self, nums, target):
        """
        Optimized version of threeSumClosest using early exits when exact match
        is found. This version also leverages the sorted array for efficient
        pointer movement.

        Time Complexity: O(n^2) Space Complexity: O(1)

        Args:
            nums: The input array of integers. target: The target sum that we
            want to get close to.

        Returns:
            The sum of the three integers closest to the target.
        """
        nums.sort()
        n = len(nums)
        closest_sum = sum(nums[:3])

        for p in range(n - 2):
            # Skip duplicates for the first element to avoid recalculating
            if p > 0 and nums[p] == nums[p - 1]:
                continue

            left, right = p + 1, n - 1

            while left < right:
                curr_sum = nums[p] + nums[left] + nums[right]

                # Early exit if we find an exact match
                if curr_sum == target:
                    return curr_sum

                # Update closestSum
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([-1, 2, 1, -4], 1, 2),  # Example 1
        ([0, 0, 0], 1, 0),       # Example 2
        ([-3, -2, -5, 3, -4], -1, -2),  # Additional test case
        ([1, 1, -1, -1, 3], -1, -1),    # Additional test case
    ]

    solution = Solution()

    for i, (numbers, t, expected) in enumerate(test_cases):
        result = solution.threeSumClosest(numbers, t)
        assert result == expected, \
            f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases passed!")
