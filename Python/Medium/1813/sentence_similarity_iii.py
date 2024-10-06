"""
1813. Sentence Similarity III

Problem Statement:
Given two sentences `sentence1` and `sentence2`, each representing a sentence composed of words, check if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal.

Constraints:
- 1 <= sentence1.length, sentence2.length <= 100
- `sentence1` and `sentence2` consist of lowercase and uppercase English letters and spaces.
- The words in `sentence1` and `sentence2` are separated by a single space.

Examples:

Example 1:
    Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
    Output: True
    Explanation: sentence2 can be turned into sentence1 by inserting "name is" between "My" and "Haley".

Example 2:
    Input: sentence1 = "of", sentence2 = "A lot of words"
    Output: False
    Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.

Example 3:
    Input: sentence1 = "Eating right now", sentence2 = "Eating"
    Output: True
    Explanation: sentence2 can be turned into sentence1 by inserting "right now" at the end of the sentence.
"""

from typing import List

class Solution:
    """
    This class implements a method to check if two sentences are similar by allowing the insertion
    of a sentence (possibly empty) into one of the sentences such that the two become equal.
    """

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        Determines whether two sentences are similar by checking if one sentence can be made equal to the other by inserting a sentence (possibly empty) in one of them.

        Time Complexity: O(n), where n is the length of the shorter sentence.
        Space Complexity: O(n), due to storing words from both sentences.

        Args:
            sentence1: str - The first sentence.
            sentence2: str - The second sentence.

        Returns:
            bool - True if one sentence can be made equal to the other by inserting a sentence, otherwise False.
        """
        s1_words: List[str] = sentence1.split(' ')
        s2_words: List[str] = sentence2.split(' ')

        start: int = 0
        ends1: int = len(s1_words) - 1
        ends2: int = len(s2_words) - 1

        # If sentence1 is longer, swap them so that s1_words is always shorter or equal in length to s2_words.
        if len(s1_words) > len(s2_words):
            return self.areSentencesSimilar(sentence2, sentence1)

        # Find maximum matching words from the start of both sentences.
        while start < len(s1_words) and s1_words[start] == s2_words[start]:
            start += 1

        # Find maximum matching words from the end of both sentences.
        while ends1 >= 0 and s1_words[ends1] == s2_words[ends2]:
            ends1 -= 1
            ends2 -= 1

        # If all remaining words are in the middle of s2, then the sentences are similar.
        return ends1 < start


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ("My name is Haley", "My Haley", True),
        ("of", "A lot of words", False),
        ("Eating right now", "Eating", True),
        ("Hello world", "Hello", True),
        ("I love programming", "I don't love programming so much", False)
    ]

    solution = Solution()

    for i, (sentence1, sentence2, expected) in enumerate(test_cases):
        result = solution.areSentencesSimilar(sentence1, sentence2)
        assert result == expected, f"Test case {i+1} failed: Expected {expected}, but got {result}"

    print("All test cases passed!")
