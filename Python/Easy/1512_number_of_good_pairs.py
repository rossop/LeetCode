"""
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Problem Link: https://leetcode.com/problems/number-of-good-pairs/

Examples:
    Example 1:
        Input: nums = [1,2,3,1,1,3]
        Output: 4
        Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

    Example 2:
        Input: nums = [1,1,1,1]
        Output: 6
        Explanation: Each pair in the array is good.

    Example 3:
        Input: nums = [1,2,3]
        Output: 0

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""

from typing import List, Dict
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Optimized Approach using a Hash Map (Counter) to count the number
        of occurrences of each number in the list. The number of good pairs
        for a number with count k is k * (k-1) // 2.

        Time Complexity: O(n), where n is the length of the input list.
        Space Complexity: O(n), due to the space used by the Counter.

        Args:
            nums (List[int]): List of integers representing the array.

        Returns:
            int: The number of good pairs in the array.
        """
        num_count: Dict[int, int] = Counter(nums)
        ans: int = 0

        for k in num_count.values():
            ans += k * (k - 1) // 2

        return ans

    def numIdenticalPairsBruteForce(self, nums: List[int]) -> int:
        """
        Brute-force approach to count all good pairs by iterating through
        all possible pairs (i, j) and checking if nums[i] == nums[j].

        Time Complexity: O(n^2), where n is the length of the input list.
        Space Complexity: O(1), since no additional space is used besides the input.

        Args:
            nums (List[int]): List of integers representing the array.

        Returns:
            int: The number of good pairs in the array.
        """
        ans: int = 0
        n: int = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    ans += 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
        ([1], 0),
        ([1, 1, 2, 3, 2, 1, 1], 8)
    ]

    for numbers, expected in test_cases:
        # Test the optimized method
        result = solution.numIdenticalPairs(numbers)
        assert result == expected, f"""
            Optimized method failed: expected {expected}, got {result}
            """

        # Test the brute-force method
        result_brute = solution.numIdenticalPairsBruteForce(numbers)
        assert result_brute == expected, f"""
            Brute-force method failed: expected {expected}, got {result_brute}
            """

    print("All test cases passed!")
