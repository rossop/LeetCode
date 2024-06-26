from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Given a non-empty array of integers nums, every element appears twice
        except for one. Find that single one.

        You must implement a solution with a linear runtime complexity and use
        only constant extra space.

        Args:
            nums (List[int]): List of integers where every element appears twice
                              except for one.

        Returns:
            int: The single element that appears only once.

        Examples:
            Example 1:
                Input: nums = [2, 2, 1]
                Output: 1

            Example 2:
                Input: nums = [4, 1, 2, 1, 2]
                Output: 4

            Example 3:
                Input: nums = [1]
                Output: 1
        """
        counts = Counter(nums)
        for num in counts:
            if counts[num] == 1:
                return num
