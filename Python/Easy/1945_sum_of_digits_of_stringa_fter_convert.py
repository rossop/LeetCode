"""
This Python file provides a solution to the LeetCode problem:

1945. Sum of Digits of String After Convert

Problem Description: You are given a string `s` consisting of lowercase English
letters, and an integer `k`.

First, convert `s` into an integer by replacing each letter with its position
in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then,
transform the integer by replacing it with the sum of its digits. Repeat the
transform operation `k` times in total.

For example, if `s = "zbax"` and `k = 2`, then the resulting integer would be 8
by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124 Transform #1: 262124 ➝ 2
+ 6 + 2 + 1 + 2 + 4 ➝ 17 Transform #2: 17 ➝ 1 + 7 ➝ 8

Return the resulting integer after performing the operations described above.

Example 1:
    Input: s = "iiii", k = 1 Output: 36

Example 2:
    Input: s = "leetcode", k = 2 Output: 6

Example 3:
    Input: s = "zbax", k = 2 Output: 8

Constraints:
    - 1 <= s.length <= 100
    - 1 <= k <= 10
    - s consists of lowercase English letters.
"""

from typing import Dict
import string


class Solution:
    """
    Provides a method to find the sum of digits of a string after converting it
    to an integer based on its alphabetical positions and performing a
    transformation operation `k` times.
    """

    def getLucky(self, s: str, k: int) -> int:
        """
        Converts a string into an integer by replacing each letter with its
        position in the alphabet, and then sums the digits of this integer `k`
        times.

        Args:
            s (str): The input string consisting of lowercase English letters.
            k (int): The number of transformations to perform.

        Returns:
            int: The resulting integer after performing the transformations.

        Time Complexity: O(n + k*m), where n is the length of the string `s`,
        and m is the number of digits in the intermediate string during
        transformation. Space Complexity: O(n) for the intermediate string
        representation.
        """

        mapping_dict: Dict[str, str] = {c: str(i + 1)
                                        for i, c in enumerate(string.ascii_lowercase)}

        def helper(s: str) -> str:
            return str(sum(int(c) for c in s))

        num = "".join(mapping_dict[c] for c in s)

        for _ in range(k):
            num = helper(num)

        return int(num)

    def getLuckyOptimised(self, s: str, k: int) -> int:
        """
        Converts a string into an integer by replacing each letter with its
        position in the alphabet, and then sums the digits of this integer `k`
        times.

        Args:
            s (str): The input string consisting of lowercase English letters.
            k (int): The number of transformations to perform.

        Returns:
            int: The resulting integer after performing the transformations.

        Time Complexity: O(n + k*m), where n is the length of the string `s`,
        and m is the number of digits in the intermediate string during
        transformation. Space Complexity: O(n) for the intermediate string
        representation.
        """

        mapping_dict: Dict[str, str] = {c: str(i + 1)
                                        for i, c in enumerate(string.ascii_lowercase)}

        def helper(s: str) -> str:
            return str(sum(int(c) for c in s))

        num = "".join(mapping_dict[c] for c in s)

        for _ in range(k):
            num = helper(num)

        return int(num)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("iiii", 1, 36),       # Example 1
        ("leetcode", 2, 6),    # Example 2
        ("zbax", 2, 8),        # Example 3
        ("a", 1, 1),           # Single character 'a' (edge case)
        ("abcdefghijklmnopqrstuvwxyz", 1, 135),  # All letters of the alphabet
    ]

    # Instantiate the solution class
    solution = Solution()

    # Loop through each test case and assert the expected output
    for i, (s, k, expected) in enumerate(test_cases):
        result = solution.getLucky(s, k)
        resultOptimised = solution.getLuckyOptimised(s, k)
        assert result == expected, \
            f"Test case {i+1} failed: Expected {expected}, but got {result}"
        assert resultOptimised == expected, \
            f"Test case {i+1} failed: Expected {expected}, but got {result}"

    print("All test cases passed!")
