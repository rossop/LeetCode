"""
1323. Maximum 69 Number
Link: https://leetcode.com/problems/maximum-69-number/

You are given a positive integer num consisting only of digits 6 and 9. 
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

TOPICS: Math, Greedy
"""

from typing import List, Dict

class Solution:
    """
    Solution class for the "Maximum 69 Number" problem.

    This class provides a method `maximum69Number` to return the maximum number
    that can be obtained by changing at most one digit (6 to 9 or 9 to 6).
    """

    def maximum69Number(self, num: int) -> int:
        """
        Finds the maximum number by changing at most one '6' to '9'.
        
        Time Complexity: O(n), where n is the number of digits in `num`.
        Space Complexity: O(n), for storing the digits.

        Args:
            num (int): The input number consisting only of digits 6 and 9.

        Returns:
            int: The maximum number obtained by changing at most one '6' to '9'.
        """
        digits: List[int] = [int(i) for i in str(num)]
        n: int = len(digits)

        for i in range(n):
            if digits[i] == 6:
                digits[i] = 9
                break
        
        return int("".join(map(str, digits)))

    def maximum69NumberOptimized(self, num: int) -> int:
        """
        Optimized approach to find the maximum number by changing the first '6' to '9'.
        
        This approach directly works with strings to avoid the overhead of list operations.

        Time Complexity: O(n), where n is the number of digits in `num`.
        Space Complexity: O(n), for storing the modified number as a string.

        Args:
            num (int): The input number consisting only of digits 6 and 9.

        Returns:
            int: The maximum number obtained by changing at most one '6' to '9'.
        """
        num_str: str = str(num)
        return int(num_str.replace('6', '9', 1))


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (9669, 9969),  # Example 1
        (9996, 9999),  # Example 2
        (9999, 9999),  # Example 3
        (6969, 9969),  # Changing the first '6' results in 9969
        (6666, 9666),  # Changing the first '6' results in 9666
    ]

    methods = [
        solution.maximum69Number,
        solution.maximum69NumberOptimized,
    ]

    for method in methods:
        for i, (num, expected) in enumerate(test_cases, 1):
            result = method(num)
            assert result == expected, f"Test case {i} failed for {method.__name__}: expected {expected}, got {result}"

    print("All test cases passed!")