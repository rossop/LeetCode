"""
242. Valid Anagram

Return whether t is an anagram of s — same characters, possibly reordered.

Problem Link: https://leetcode.com/problems/valid-anagram/

Examples:
    Example 1:
        Input: s = "racecar", t = "carrace"
        Output: true

    Example 2:
        Input: s = "jar", t = "jam"
        Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Sort both strings and compare. Cheapest to write; pays a log factor
        you don't strictly need.

        Time complexity:  O(n log n)
        Space complexity: O(n) — sorted() materializes lists.
        """
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    def isAnagramCounter(self, s: str, t: str) -> bool:
        """
        Character-frequency equality via Counter. Two counters are equal iff
        every key maps to the same count, so this captures anagram-ness in
        a single comparison.

        Time complexity:  O(n)
        Space complexity: O(k), k = alphabet size (26 here, so O(1)).
        """
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
        ("a", "a", True),
        ("ab", "ba", True),
        ("abc", "cba", True),
        ("abc", "abcd", False),
        ("racecar", "carrace", True),
        ("jar", "jam", False),
    ]

    for i, (s, t, expected) in enumerate(test_cases, 1):
        assert solution.isAnagram(s, t) == expected, f"isAnagram test {i} failed"
        assert solution.isAnagramCounter(s, t) == expected, f"isAnagramCounter test {i} failed"

    print("All test cases passed!")
