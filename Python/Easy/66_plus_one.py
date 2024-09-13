"""
6. Plus One

Problem Statement: You are given a large integer represented as an integer
array digits, where each digits[i] is the ith digit of the integer. The digits
are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
    Input: digits = [1, 2, 3] Output: [1, 2, 4] Explanation: The array
    represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus,
    the result should be [1, 2, 4].

Example 2:
    Input: digits = [4, 3, 2, 1] Output: [4, 3, 2, 2] Explanation: The array
    represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322.
    Thus, the result should be [4, 3, 2, 2].

Example 3:
    Input: digits = [9] Output: [1, 0] Explanation: The array represents the
    integer 9. Incrementing by one gives 9 + 1 = 10. Thus, the result should be
    [1, 0].

Constraints:
    - 1 <= digits.length <= 100
    - 0 <= digits[i] <= 9
    - digits does not contain any leading 0's.
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Converts the digits array to an integer, adds one, and then converts it
        back to an array.

        Time Complexity: O(n), where n is the number of digits. Space
        Complexity: O(n), where n is the size of the input digits.

        Args:
            digits: A list of integers representing a large number.

        Returns:
            A list of integers representing the number incremented by one.
        """
        # Convert the digits to a string, then to an integer,
        # add 1, and convert back to list of digits
        digits = [*map(str, digits)]
        num: int = int("".join(digits))
        num += 1
        return list(map(int, str(num)))

    def plusOneOptimized(self, digits: List[int]) -> List[int]:
        """
        Optimized solution that avoids converting to a string and back by
        handling carry manually.

        Time Complexity: O(n), where n is the number of digits. Space
        Complexity: O(1) additional space (modifies the input list in-place).

        Args:
            digits: A list of integers representing a large number.

        Returns:
            A list of integers representing the number incremented by one.
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, we can increment it and
            # return the result.
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise, set the current digit to 0 and continue to handle the
            # carry.
            digits[i] = 0

        # If all digits were 9, the result will be 100...0 (with an extra 1 at
        # the beginning).
        return [1] + digits


if __name__ == "__main__":
    # Example test cases
    solution = Solution()

    # Test cases with assertions
    test_cases = [
        ([1, 2, 3], [1, 2, 4]),        # Example 1
        ([4, 3, 2, 1], [4, 3, 2, 2]),  # Example 2
        ([9], [1, 0]),                 # Example 3
        ([9, 9], [1, 0, 0]),           # Case with carryover at multiple digits
        ([1, 9, 9], [2, 0, 0])         # Case with carryover in the middle
    ]

    for i, (digits, expected) in enumerate(test_cases):
        result = solution.plusOne(digits.copy())
        assert result == expected, \
            (f"Test case {i + 1} failed for plusOne."
                f" Expected {expected}, got {result}.")

        result_optimized = solution.plusOneOptimized(digits.copy())
        assert result_optimized == expected, \
            (f"Test case {i + 1} failed for plusOneOptimized."
                f" Expected {expected}, got {result_optimized}.")

        print(f"Test case {i + 1} passed for both methods!")

    print("All test cases passed!")
