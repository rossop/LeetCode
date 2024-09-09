from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the
        longest consecutive elements sequence.

        You must write an algorithm that runs in O(n) time.

        Args:
            nums (List[int]): An unsorted list of integers.

        Returns:
            int: The length of the longest consecutive elements sequence.

        Examples:
            Example 1:
                Input: nums = [100, 4, 200, 1, 3, 2]
                Output: 4
                Explanation: The longest consecutive elements sequence is
                       [1, 2, 3, 4].
                Therefore its length is 4.

            Example 2:
                Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
                Output: 9
                Explanation: The longest consecutive elements sequence is
                        [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore its length is 9.
        """
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:  # if num is the start of a sequence
                curr = 1
                while num + 1 in s:
                    curr += 1
                    num += 1
                longest = max(longest, curr)

        return longest
