"""
1930. Unique Length-3 Palindromic Subsequences

Problem Statement:
Given a string s, return the number of unique palindromes of length three that
are a subsequence of s. Even if there are multiple ways to obtain the same
subsequence, it is still only counted once.

Constraints:
- 3 <= s.length <= 10^5
- s consists of only lowercase English letters.

Examples:

Example 1:
    Input: s = "aabca"
    Output: 3
    Explanation: "aba", "aaa", "aca"

Example 2:
    Input: s = "adc"
    Output: 0

Example 3:
    Input: s = "bbcbaba"
    Output: 4
    Explanation: "bbb", "bcb", "bab", "aba"
"""

from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Counts unique length-3 palindromic subsequences using first/last occurrence.

        A length-3 palindrome has the form X_Y_X where X is the outer character
        and Y is any character strictly between the first and last occurrence of X.
        For each unique character ch in s, finds its leftmost and rightmost positions.
        Any character in s[left+1:right] can serve as the middle, and each unique
        middle character produces a distinct palindrome. Summing these counts gives
        the total.

        Time complexity:  O(26 * n) = O(n) — at most 26 characters, each requiring
                          a linear scan for first/last occurrence and unique middle chars.
        Space complexity: O(1) — set of middle characters is bounded by 26.
        """
        res: int = 0

        for ch in set(s):
            left: int = s.find(ch)
            right: int = s.rfind(ch)

            if right - left >= 2:
                res += len(set(s[left + 1:right]))

        return res

    def countPalindromicSubsequenceCounter(self, s: str) -> int:
        """
        Counts unique length-3 palindromic subsequences using a sliding Counter.

        Maintains a left set of characters seen so far and a right Counter of
        characters yet to be seen. For each middle character m, any character c
        in left that also appears in right forms a valid palindrome c_m_c.
        Stores each (m, c) pair in a result set to deduplicate.

        The right Counter is decremented before each inner check so that the
        current m is not counted as a future outer character at the same position.

        Time complexity:  O(26 * n) = O(n) — inner loop over left is bounded by 26.
        Space complexity: O(26) = O(1) — left set and result set bounded by alphabet size.
        """
        res = set()
        left = set()
        right = Counter(s)

        for m in s:
            right[m] -= 1
            for c in left:
                if right[c] > 0:
                    res.add((m, c))
            left.add(m)

        return len(res)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("aabca",   3),
        ("adc",     0),
        ("bbcbaba", 4),
        ("aaaa",    1),
        ("abc",     0),
    ]

    for label, method in [
        ("countPalindromicSubsequence       ", solution.countPalindromicSubsequence),
        ("countPalindromicSubsequenceCounter", solution.countPalindromicSubsequenceCounter),
    ]:
        for s, expected in test_cases:
            result = method(s)
            assert result == expected, \
                f"{label} failed on {s!r}: expected {expected}, got {result}"
        print(f"  {label} passed")

    print("All test cases passed!")
