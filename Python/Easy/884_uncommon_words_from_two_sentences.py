"""
884. Uncommon Words from Two Sentences

Problem Statement: A sentence is a string of single-space separated words where
each word consists only of lowercase letters. A word is uncommon if it appears
exactly once in one of the sentences, and does not appear in the other
sentence.

Given two sentences `s1` and `s2`, return a list of all the uncommon words. You
may return the answer in any order.

Example 1:
    Input: s1 = "this apple is sweet", s2 = "this apple is sour" Output:
    ["sweet","sour"]

Example 2:
    Input: s1 = "apple apple", s2 = "banana" Output: ["banana"]

Constraints: - 1 <= s1.length, s2.length <= 200 - s1 and s2 consist of
lowercase English letters and spaces. - s1 and s2 do not have leading or
trailing spaces. - All the words in `s1` and `s2` are separated by a single
space.
"""

from typing import List, Dict


class Solution:
    """
    This class provides a method to find uncommon words from two sentences.
    """
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        Returns a list of words that appear exactly once in either s1 or s2,
        but not both.

        Time Complexity: O(n), where n is the total number of words in both
        sentences. Space Complexity: O(n), due to the dictionary that stores
        the word counts.

        Args:
            s1: str - The first sentence. s2: str - The second sentence.

        Returns:
            List[str] - A list of uncommon words.
        """
        # Dictionary to store the count of each word
        word_hash: Dict[str, int] = {}

        # Split sentences into lists of words
        words1: List[str] = s1.split()
        words2: List[str] = s2.split()

        # Combine the words from both sentences
        words = words1 + words2

        # Count occurrences of each word
        for word in words:
            word_hash[word] = word_hash.get(word, 0) + 1

        # Return words that occur exactly once
        return [word for word, cnt in word_hash.items() if cnt == 1]


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
        ("apple apple", "banana", ["banana"]),
        ("a b c", "a b d", ["c", "d"]),
    ]

    solution = Solution()

    for i, (string1, string2, expected) in enumerate(test_cases):
        result = solution.uncommonFromSentences(string1, string2)
        assert sorted(result) == sorted(expected), \
            f"Test case {i+1} failed: Expected {expected}, but got {result}"

    print("All test cases passed!")
