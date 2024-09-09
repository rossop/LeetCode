from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Given a binary array nums, return the maximum number of consecutive 1's
        in the array.

        Args:
            nums (List[int]): A list of binary integers (0s and 1s).

        Returns:
            int: The maximum number of consecutive 1's in the array.

        Examples:
            Example 1:
                Input: nums = [1, 1, 0, 1, 1, 1]
                Output: 3
                Explanation: The first two digits or the last three digits are
                             consecutive 1s.
                             The maximum number of consecutive 1s is 3.

            Example 2:
                Input: nums = [1, 0, 1, 1, 0, 1]
                Output: 2
                Explanation: The maximum number of consecutive 1s is 2.
        """
        max_count = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)   # max has O(1) time complex
            else:
                count = 0

        return max_count

# Example usage:
solution = Solution()
print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # Output: 3
print(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # Output: 2
