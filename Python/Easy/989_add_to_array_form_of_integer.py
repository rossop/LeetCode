"""
989. Add to Array-Form of Integer

Problem Statement: The array-form of an integer num is an array representing
its digits in left to right order. For example, for num = 1321, the array form
is [1,3,2,1]. Given num, the array-form of an integer, and an integer k, return
the array-form of the integer num + k.

Example 1:
    Input: num = [1, 2, 0, 0], k = 34 Output: [1, 2, 3, 4] Explanation: 1200 +
    34 = 1234

Example 2:
    Input: num = [2, 7, 4], k = 181 Output: [4, 5, 5] Explanation: 274 + 181 =
    455

Example 3:
    Input: num = [2, 1, 5], k = 806 Output: [1, 0, 2, 1] Explanation: 215 + 806
    = 1021

Constraints: - 1 <= num.length <= 10^4 - 0 <= num[i] <= 9 - num does not
contain any leading zeros except for the zero itself. - 1 <= k <= 10^4
"""

from typing import List


class Solution:
    """
    This class contains a method to add an integer `k` to an array-form integer
    `num`.

    Method:
    -  addToArrayForm: Adds an integer `k` to the array-form of `num`.
    """

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """
        Adds the integer `k` to the array-form of the integer `num`.

        Time Complexity: O(max(len(num), len(k_list))), where k_list is the
        digit representation of k.
        Space Complexity: O(max(len(num), len(k_list))), for storing the result

        Args:
            num: List[int] - The array-form of the integer. k: int - The
            integer to add to `num`.

        Returns:
            List[int] - The array-form of the result after adding `k`.
        """
        # Convert `k` into an array-form by turning it into a string and
        # then converting each character back to an integer
        k_list: List[int] = [int(c) for c in str(k)]
        # Initialize pointers to traverse `num` and `k_list`
        i, j = len(num) - 1, len(k_list) - 1
        carry: int = 0
        result: List[int] = []

        # Traverse both `num` and `k_list` from the right to the left
        while i >= 0 or j >= 0 or carry:
            # Get the current values from `num` and `k_list`
            # or 0 if out of bounds
            val1: int = num[i] if i >= 0 else 0
            val2: int = k_list[j] if j >= 0 else 0

            # Calculate the total value and carry
            total: int = val1 + val2 + carry
            carry = total // 10  # Update the carry
            # Append the last digit of the total to the result
            result.append(total % 10)

            # Move to the next digits
            i -= 1
            j -= 1

        # The result is built from right to left, so we reverse it
        # before returning
        return result[::-1]


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 0, 0], 34, [1, 2, 3, 4]),
        ([2, 7, 4], 181, [4, 5, 5]),
        ([2, 1, 5], 806, [1, 0, 2, 1]),
        ([9, 9, 9, 9], 1, [1, 0, 0, 0, 0]),
    ]

    solution = Solution()

    for ii, (numm, kk, expected) in enumerate(test_cases):
        res = solution.addToArrayForm(numm, kk)
        assert res == expected, \
            f"Test case {ii+1} failed: Expected {expected}, but got {res}"

    print("All test cases passed!")
