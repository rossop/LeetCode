
"""
670. Maximum Swap

Problem Statement:
You are given an integer num. You can swap two digits at most once to get the
maximum valued number. Return the maximum valued number you can get.

Examples:

Example 1:
    Input: num = 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.

Example 2:
    Input: num = 9973
    Output: 9973
    Explanation: No swap.

Constraints:
- 0 <= num <= 10^8
"""
from typing import List


class Solution:
    """
    This class provides two methods to solve the problem of finding the maximum
    number that can be obtained by swapping two digits at most once.
    """

    def maximumSwap(self, num: int) -> int:
        """
        This method converts the integer num into a list of its digits, and
        then scans the list from right to left to determine the largest
        possible number by performing a single swap.

        Time Complexity: O(n), where n is the number of digits in num.
        Space Complexity: O(n) for storing the digits of num as a list.

        Args:
            num (int): The input integer.

        Returns:
            int: The maximum number after performing at most one swap.
        """
        num_list: List[str] = list(str(num))
        max_digit: str = "0"

        max_i: int = -1
        swap_i: int = -1
        swap_j: int = -1

        for i in reversed(range(len(num_list))):
            # Track the largest digit found as we traverse from right to left
            if num_list[i] > max_digit:
                max_digit = num_list[i]
                max_i = i
            # If we find a smaller digit, we mark it as a candidate
            # for swapping
            if num_list[i] < max_digit:
                swap_i, swap_j = i, max_i

        # If a swap is possible, perform it
        if swap_i != -1:
            num_list[swap_i], num_list[swap_j] = \
                num_list[swap_j], num_list[swap_i]

        return int("".join(num_list))

    def maximumSwapAlternative(self, num: int) -> int:
        """
        This method uses a dictionary to record the last occurrence of each
        digit. It then tries to find the first larger digit after each digit in
        num to perform a swap.

        Time Complexity: O(n), where n is the number of digits in num.
        Space Complexity: O(n) for storing the last occurrence dictionary and
        the list of digits.

        Args:
            num (int): The input integer.

        Returns:
            int: The maximum number after performing at most one swap.
        """
        num_list: List[int] = [int(c) for c in str(num)]
        last_occurrence: dict = {digit: i for i, digit in enumerate(num_list)}

        # Traverse each digit in num_list
        for i, digit in enumerate(num_list):
            # Try to find a larger digit to swap with, starting from 9 down to
            # digit + 1
            for larger_digit in range(9, digit, -1):
                if larger_digit in last_occurrence \
                        and last_occurrence[larger_digit] > i:
                    # Swap the current digit with the larger digit found
                    swap_index: int = last_occurrence[larger_digit]
                    num_list[i], num_list[swap_index] = \
                        num_list[swap_index], num_list[i]
                    # Return the new number as an integer
                    return int(''.join(map(str, num_list)))

        # If no swap was made, return the original number
        return num


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: num = 2736
    result: int = solution.maximumSwap(2736)
    assert result == 7236, f"Test Case 1 Failed! Got {result}"

    # Test Case 2: num = 9973
    result = solution.maximumSwap(9973)
    assert result == 9973, f"Test Case 2 Failed! Got {result}"

    # Test Case 3: num = 1993
    result = solution.maximumSwap(1993)
    assert result == 9913, f"Test Case 3 Failed! Got {result}"

    # Test Case 4: num = 98368
    result = solution.maximumSwap(98368)
    assert result == 98863, f"Test Case 4 Failed! Got {result}"

    # Test Case 5: num = 12345
    result = solution.maximumSwap(12345)
    assert result == 52341, f"Test Case 5 Failed! Got {result}"

    print("All test cases passed!")
