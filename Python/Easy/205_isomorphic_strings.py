"""
205. Isomorphic Strings
Link: https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

TOPICS: Hash Table, String
"""

from typing import Dict

class Solution:
    """
    Solution class for the "Isomorphic Strings" problem.

    This class provides a method `isIsomorphic` to determine if two strings `s` and `t` are isomorphic.
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determines if two strings `s` and `t` are isomorphic.

        Two strings are isomorphic if the characters in `s` can be replaced to get `t`,
        with each character in `s` mapping to exactly one character in `t`, and no two
        characters in `s` mapping to the same character in `t`.

        Time Complexity: O(n), where n is the length of the strings `s` and `t`.
        Space Complexity: O(n), for storing the mappings in two dictionaries.

        Args:
            s (str): The first input string.
            t (str): The second input string.

        Returns:
            bool: True if the strings are isomorphic, False otherwise.
        """
        # Early exit if the strings are not of the same length
        if len(s) != len(t):
            return False
        
        # Create two dictionaries for bidirectional mapping
        s_to_t: Dict[str, str] = {}
        t_to_s: Dict[str, str] = {}

        # Iterate over characters of both strings
        for s_char, t_char in zip(s, t):
            # Check the mapping from s to t
            if s_char in s_to_t:
                if s_to_t[s_char] != t_char:
                    return False
            else:
                s_to_t[s_char] = t_char

            # Check the mapping from t to s
            if t_char in t_to_s:
                if t_to_s[t_char] != s_char:
                    return False
            else:
                t_to_s[t_char] = s_char

        # If no mismatches were found, the strings are isomorphic
        return True


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("egg", "add", True),  # Example 1
        ("foo", "bar", False),  # Example 2
        ("paper", "title", True),  # Example 3
        ("badc", "baba", False),  # The problematic case
        ("aab", "xyz", False),  # Edge case where the characters don't map one-to-one
        ("ab", "aa", False),  # Edge case where two different chars in `s` map to the same in `t`
    ]
    
    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = solution.isIsomorphic(s, t)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    
    print("All test cases passed!")