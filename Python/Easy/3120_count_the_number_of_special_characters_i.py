"""
3120. Count the Number of Special Characters I

You are given a string word. A letter is called special if it appears both in
lowercase and uppercase in word. Return the number of special letters in word.

Problem Link: https://leetcode.com/problems/count-the-number-of-special-characters-i/

Examples:
    Example 1:
        Input: word = "aaAbcBC"
        Output: 3
        Explanation: The special characters are 'a', 'b', and 'c'.

    Example 2:
        Input: word = "abc"
        Output: 0
        Explanation: No character appears in uppercase.

    Example 3:
        Input: word = "abBCab"
        Output: 1
        Explanation: The only special character is 'b'.

Constraints:
    1 <= word.length <= 50
    word consists of only lowercase and uppercase English letters.
"""

import string


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        Collapse word to a set of distinct characters, then count lowercase
        letters whose uppercase form is also present.

        Time complexity:  O(n)
        Space complexity: O(1) — the set holds at most 52 letters.
        """
        char_set: set[str] = set(word)
        ans: int = 0
        for c in char_set:
            if c.islower() and c.upper() in char_set:
                ans += 1
        return ans

    def numberOfSpecialCharsAscii(self, word: str) -> int:
        """
        Same set membership idea, but iterate the 26 lowercase letters
        directly so the result is independent of set iteration order.

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        s: set[str] = set(word)
        return sum(c in s and c.upper() in s for c in string.ascii_lowercase)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("aaAbcBC", 3),
        ("abc", 0),
        ("abBCab", 1),
        ("a", 0),
        ("aA", 1),
        ("AaBbCc", 3),
    ]

    for i, (word, expected) in enumerate(test_cases, 1):
        assert solution.numberOfSpecialChars(word) == expected, f"set test {i} failed: {word!r}"
        assert solution.numberOfSpecialCharsAscii(word) == expected, f"ascii test {i} failed: {word!r}"

    print("All test cases passed!")
