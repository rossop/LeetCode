"""
2942. Find Words Containing Character

Given a 0-indexed array of strings 'words' and a character 'x',
return an array of indices representing the words that contain
the character 'x'.

Note that the returned array may be in any order.

Problem Link: https://leetcode.com/problems/find-words-containing-character/

Example 1:
    Input: words = ["leet","code"], x = "e"
    Output: [0, 1]
    Explanation: "e" occurs in both words: "leet", and "code". Hence, we
    return indices 0 and 1.

Example 2:
    Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
    Output: [0, 2]
    Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices
    0 and 2.

Example 3:
    Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
    Output: []
    Explanation: "z" does not occur in any of the words. Hence, we return
    an empty array.

Constraints:
    - 1 <= words.length <= 50
    - 1 <= words[i].length <= 50
    - x is a lowercase English letter.
    - words[i] consists only of lowercase English letters.
"""
from typing import List


class Solution:

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """
        This method finds all the indices of words in the given list that
        contain the character 'x'.

        Time Complexity: O(n * m), where n is the number of words and m is
        the average length of the words.
        Space Complexity: O(k), where k is the number of words containing
        the character x.

        Args:
        words (List[str]): List of words.
        x (str): The character to check for in each word.

        Returns:
        List[int]: List of indices of words containing the character 'x'.
        """
        wordCount: List[int] = []
        for pos, w in enumerate(words):
            if x in w:
                wordCount.append(pos)
        return wordCount


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (["leet", "code"], "e", [0, 1]),        # Test case 1
        (["abc", "bcd", "aaaa", "cbc"], "a", [0, 2]),  # Test case 2
        (["abc", "bcd", "aaaa", "cbc"], "z", []),     # Test case 3
    ]

    for i, (words, x, expected) in enumerate(test_cases, 1):
        result = solution.findWordsContaining(words, x)
        assert sorted(result) == sorted(expected), f"""
        Test case {i} failed: expected {expected}, got {result}"""
        print(f"Test case {i} passed!")

    print("All test cases passed!")
