"""
214. Shortest Palindrome

Problem Statement:
You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.

Example 1:
    Input: s = "aacecaaa"
    Output: "aaacecaaa"

Example 2:
    Input: s = "abcd"
    Output: "dcbabcd"

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of lowercase English letters only.
"""

from typing import List

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Optimized version using KMP algorithm.
        Finds the shortest palindrome by adding characters in front of the input string.

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(n), due to the space needed for the KMP table.

        Args:
            s: str - The input string.

        Returns:
            str - The shortest palindrome formed by adding characters in front of the string.
        """
        if not s:
            return s

        # Create a concatenated string with s + '#' + reverse(s)
        rev_s = s[::-1]
        concat = s + '#' + rev_s

        # Build the KMP table for the concatenated string
        n = len(concat)
        kmp_table = [0] * n
        j = 0  # Length of the previous longest prefix suffix

        # Build the KMP table
        for i in range(1, n):
            while j > 0 and concat[i] != concat[j]:
                j = kmp_table[j - 1]
            if concat[i] == concat[j]:
                j += 1
            kmp_table[i] = j

        # The value in kmp_table[-1] gives us the length of the longest palindrome prefix
        longest_palindromic_prefix_len = kmp_table[-1]

        # Characters that need to be added to the front to make the string a palindrome
        suffix_to_add = rev_s[:len(s) - longest_palindromic_prefix_len]

        # Return the shortest palindrome
        return suffix_to_add + s

    def shortestPalindromeBruteForce(self, s: str) -> str:
        """
        Brute-force version (User's original solution).
        Finds the shortest palindrome by adding characters in front of the input string.

        Time Complexity: O(n^2), where n is the length of the string due to checking for palindrome at each point.
        Space Complexity: O(n), to store the result.

        Args:
            s: str - The input string.

        Returns:
            str - The shortest palindrome formed by adding characters in front of the string.
        """

        def is_pali(s: str, l: int, r: int) -> bool:
            """Helper function to check if a substring is a palindrome."""
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        n = len(s)

        # Try to find the longest palindromic prefix
        for r in reversed(range(n)):
            if is_pali(s, 0, r):
                suffix = s[r + 1:]
                return suffix[::-1] + s

        return ""


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ("aacecaaa", "aaacecaaa"),
        ("abcd", "dcbabcd"),
        ("", ""),
        ("a", "a"),
        ("racecar", "racecar"),
    ]

    solution = Solution()

    # Test the optimized method
    print("Testing Optimized Method:")
    for i, (input_str, expected) in enumerate(test_cases):
        result = solution.shortestPalindrome(input_str)
        assert result == expected, f"Test case {i+1} failed (Optimized): Expected {expected}, but got {result}"
    print("All test cases passed for Optimized Method!")

    # Test the brute-force method
    print("\nTesting Brute-force Method:")
    for i, (input_str, expected) in enumerate(test_cases):
        result = solution.shortestPalindromeBruteForce(input_str)
        assert result == expected, f"Test case {i+1} failed (Brute-force): Expected {expected}, but got {result}"
    print("All test cases passed for Brute-force Method!")
