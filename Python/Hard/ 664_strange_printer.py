"""
664. Strange Printer
Link: https://leetcode.com/problems/strange-printer/

There is a strange printer with the following two special properties:
1. The printer can only print a sequence of the same character each time.
2. At each turn, the printer can print new characters starting from and ending at any place 
   and will cover the original existing characters.

Given a string s, return the minimum number of turns the printer needed to print it.

Example 1:
Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".

Example 2:
Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, 
             which will cover the existing character 'a'.

Constraints:
1 <= s.length <= 100
s consists of lowercase English letters.
"""

from typing import Dict, List
from collections import defaultdict

class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        Calculate the minimum number of turns the strange printer needs to print the string s.

        The function uses dynamic programming with memoization to solve the problem efficiently.

        Args:
            s (str): The input string.

        Returns:
            int: The minimum number of turns required to print the string.

        Time Complexity: O(n^3), where n is the length of the string.
        Space Complexity: O(n^2) for storing the DP results in the `visited` dictionary.
        """
        visited: Dict[int, int] = defaultdict(int)

        def printer(i: int, j: int) -> int:
            """
            Recursive helper function to calculate the minimum number of turns to print s[i:j+1].

            Args:
                i (int): The starting index of the substring.
                j (int): The ending index of the substring.

            Returns:
                int: The minimum number of turns required to print s[i:j+1].
            """
            if i > j:
                return 0

            if (i, j) in visited:
                return visited[(i, j)]
            
            # Minimize the number of turns by considering all possible split points
            res = 1 + printer(i + 1, j)
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    res = min(res, printer(i, k - 1) + printer(k + 1, j))
            
            visited[(i, j)] = res
            return res

        return printer(0, len(s) - 1)


if __name__ == "__main__":
    # Test cases to validate the solution
    solution = Solution()
    test_cases = [
        ("aaabbb", 2),
        ("aba", 2),
        ("a", 1),
        ("abcba", 3),
        ("ababab", 4),
        ("aabbcc", 3),
        ("abcabcabc", 7)
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.strangePrinter(s)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")