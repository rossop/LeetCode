"""
58. Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
NOTE: This is a missed chance since Luffy's number is 56, not 58 like this question.

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
TOPICS: String
"""

class Solution:
    """
    Solution class for the "Length of Last Word" problem.

    This class provides two methods to return the length of the last word in the string:
    1. `lengthOfLastWord`: The initial solution using string split.
    2. `lengthOfLastWordOptimized`: An optimized solution that iterates from the end.
    """

    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in the given string `s`.
        
        This method splits the string by whitespace, extracts the last word, and returns its length.

        Time Complexity: O(n), where n is the length of the string `s`.
        Space Complexity: O(n), for storing the words in a list.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the last word in the string.
        """
        words = s.split()
        return len(words[-1]) if words else 0

    def lengthOfLastWordOptimized(self, s: str) -> int:
        """
        Returns the length of the last word in the given string `s`.

        This method iterates through the string from the end to find the last word
        without splitting the string, making it more efficient.

        Time Complexity: O(n), where n is the length of the string `s`.
        Space Complexity: O(1), as no extra space is required apart from a few variables.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the last word in the string.
        """
        length = 0
        i = len(s) - 1

        # Skip trailing spaces at the end
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Count the length of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("Hello World", 5),  # Example 1
        ("   fly me   to   the moon  ", 4),  # Example 2
        ("luffy is still joyboy", 6),  # Example 3
        ("a", 1),  # Single word with one character
        (" ", 0),  # Only spaces
        ("day   ", 3),  # Trailing spaces
    ]
    
    methods = [
        solution.lengthOfLastWord,
        solution.lengthOfLastWordOptimized,
    ]

    for method in methods:
        for i, (s, expected) in enumerate(test_cases, 1):
            result = method(s)
            assert result == expected, f"Test case {i} failed for {method.__name__}: expected {expected}, got {result}"
    
    print("All test cases passed!")