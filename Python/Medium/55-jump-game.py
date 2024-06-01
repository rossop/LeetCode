from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Given an array of non-negative integers nums, where each element represents your
        maximum jump length at that position, return true if you can reach the last index,
        or false otherwise.

        Args:
            nums (List[int]): A list of non-negative integers representing jump lengths.

        Returns:
            bool: True if you can reach the last index, False otherwise.

        Examples:
            Example 1:
                Input: nums = [2, 3, 1, 1, 4]
                Output: True
                Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

            Example 2:
                Input: nums = [3, 2, 1, 0, 4]
                Output: False
                Explanation: You will always arrive at index 3 no matter what. Its maximum
                             jump length is 0, which makes it impossible to reach the last index.
        """
        n = len(nums)
        goal = n - 1

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= goal:       # nums[i] pulls the maximum jump
                goal = i

        return goal == 0

# Example usage:
solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]))  # Output: True
print(solution.canJump([3, 2, 1, 0, 4]))  # Output: False
