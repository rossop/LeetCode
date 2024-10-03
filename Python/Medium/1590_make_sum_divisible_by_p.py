"""
1590. Make Sum Divisible by P

Problem Statement:
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining
elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= p <= 10^9

Example 1:
    Input: nums = [3, 1, 4, 2], p = 6
    Output: 1
    Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4],
    and the sum of the remaining elements is 6, which is divisible by 6.

Example 2:
    Input: nums = [6, 3, 5, 2], p = 9
    Output: 2
    Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5, 2],
    leaving us with [6, 3] with sum 9.

Example 3:
    Input: nums = [1, 2, 3], p = 3
    Output: 0
    Explanation: The sum is 6, which is already divisible by 3. Thus we do not need to remove anything.
"""

from typing import List, Dict

class Solution:
    """
    This class implements a method to remove the smallest subarray such that the remaining elements' sum
    is divisible by p.
    """

    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        Finds the length of the smallest subarray that, when removed, makes the sum of the remaining elements
        divisible by p. If no such subarray can be found, returns -1.

        Time Complexity: O(n), where n is the length of nums. We loop through the array once.
        Space Complexity: O(n), due to the usage of a hash map to store the current modulo results.

        Args:
            nums: List[int] - The input list of integers.
            p: int - The integer by which the remaining sum should be divisible.

        Returns:
            int - The length of the smallest subarray to remove, or -1 if impossible.
        """
        n: int = len(nums)
        total_sum: int = sum(nums) % p  # Total sum modulo p

        # If the total sum is already divisible by p, no subarray needs to be removed.
        if total_sum == 0:
            return 0

        # Dictionary to store moduli of prefix sums with their respective indices
        mod_map: Dict[int, int] = {0: -1}  # To handle the case where the subarray starts from the beginning
        current_sum: int = 0
        min_len: int = n  # Initialize the min_len as n (worst case if no subarray is found)

        # Traverse through the nums array
        for i in range(n):
            current_sum = (current_sum + nums[i]) % p
            needed: int = (current_sum - total_sum + p) % p  # The target mod we need to find in mod_map

            # If the needed mod is found in the map, calculate the subarray length
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])

            # Update the map with the current mod and its index
            mod_map[current_sum] = i

        # If no valid subarray is found, return -1. Otherwise, return the smallest length found.
        return -1 if min_len == n else min_len


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ([3, 1, 4, 2], 6, 1),  # Remove subarray [4]
        ([6, 3, 5, 2], 9, 2),  # Remove subarray [5, 2]
        ([1, 2, 3], 3, 0),     # Already divisible by 3, no removal needed
        ([1, 2, 3, 10], 7, 1),  # Remove [10]
    ]

    solution = Solution()

    for i, (nums, p, expected) in enumerate(test_cases):
        result = solution.minSubarray(nums, p)
        assert result == expected, f"Test case {i+1} failed: Expected {expected}, but got {result}"

    print("All test cases passed!")
