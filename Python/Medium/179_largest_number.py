"""
179. Largest Number

Problem Statement: Given a list of non-negative integers nums, arrange them
such that they form the largest number and return it.

Since the result may be very large, you need to return a string instead of an
integer.

Example 1:
    Input: nums = [10, 2] Output: "210"

Example 2:
    Input: nums = [3, 30, 34, 5, 9] Output: "9534330"

Constraints: - 1 <= nums.length <= 100 - 0 <= nums[i] <= 10^9
"""

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Returns the largest number that can be formed by arranging the given
        numbers.

        Time Complexity: O(n log n), where n is the length of nums due to
        sorting. Space Complexity: O(n), due to the space used to store the
        strings and result.

        Args:
            nums: List[int] - A list of non-negative integers.

        Returns:
            str - The largest number formed as a string.
        """
        # Convert the numbers to strings to facilitate comparison
        nums: List[str] = list(map(str, nums))

        # Custom comparator function to sort numbers based on their
        # concatenation
        def compare(n1: str, n2: str) -> int:
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        # Sort the numbers using the custom comparator
        nums = sorted(nums, key=cmp_to_key(compare))

        # Join the numbers to form the largest number and handle the case of
        # leading zeros
        return str(int("".join(nums)))


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ([10, 2], "210"),
        ([3, 30, 34, 5, 9], "9534330"),
        ([0, 0], "0"),
        ([1, 10, 100], "110100"),
    ]

    solution = Solution()

    for i, (numbers, expected) in enumerate(test_cases):
        result = solution.largestNumber(numbers)
        assert result == expected, \
            f"Test case {i+1} failed: Expected {expected}, but got {result}"

    print("All test cases passed!")
