"""
1684. Count the Number of Consistent Strings

Problem Statement:
You are given a string `allowed` consisting of distinct characters and an array of 
strings `words`. A string is consistent if all characters in the string appear 
in the string `allowed`.

Return the number of consistent strings in the array `words`.

Constraints:
- 1 <= words.length <= 10^4
- 1 <= allowed.length <= 26
- 1 <= words[i].length <= 10
- The characters in `allowed` are distinct.
- words[i] and allowed contain only lowercase English letters.

Example 1:
    Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    Output: 2
    Explanation: Strings "aaab" and "baa" are consistent since they only 
    contain characters 'a' and 'b'.

Example 2:
    Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
    Output: 7
    Explanation: All strings are consistent.

Example 3:
    Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
    Output: 4
    Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

"""

from typing import List, Set

class Solution:
    """
    A class used to count the number of consistent strings in a list of words, 
    given a set of allowed characters.
    """

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        Count how many words are consistent based on the allowed characters.
        A word is consistent if all of its characters appear in the allowed string.
        
        Time Complexity: O(m * n), where n is the number of words, and m is the 
        average length of each word.
        
        Space Complexity: O(m), where m is the number of unique characters in 
        the `allowed` string.
        
        Args:
            allowed: A string containing distinct characters allowed in words.
            words: A list of words to check for consistency.
        
        Returns:
            The number of consistent strings.
        """
        allowed_set: Set[str] = set(allowed)

        def is_consistent(word: str) -> bool:
            return set(word).issubset(allowed_set)

        return sum(is_consistent(word) for word in words)

    def countConsistentStringsOptimized(self, allowed: str, words: List[str]) -> int:
        """
        Optimized approach to count the number of consistent strings using bit 
        manipulation. The idea is to treat allowed characters as bits in an integer.
        
        Time Complexity: O(m + n), where n is the number of words and m is the 
        length of the allowed string.
        
        Space Complexity: O(1), since the bitmask uses constant space.
        
        Args:
            allowed: A string containing distinct characters allowed in words.
            words: A list of words to check for consistency.
        
        Returns:
            The number of consistent strings.
        """
        # Create a bitmask for the allowed string
        allowed_mask: int = 0
        for char in allowed:
            allowed_mask |= 1 << (ord(char) - ord('a'))

        def is_consistent(word: str) -> bool:
            # Create a bitmask for the word
            for char in word:
                if not (allowed_mask & (1 << (ord(char) - ord('a')))):
                    return False
            return True

        return sum(is_consistent(word) for word in words)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),  # Example 1
        ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),  # Example 2
        ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4),  # Example 3
        ("xyz", ["x", "xy", "yz", "y"], 4),  # Custom Test Case 1
        ("abc", ["def", "ghi", "jkl"], 0),  # Custom Test Case 2
    ]

    # Instantiate the solution class
    solution = Solution()

    # Loop through each test case
    for i, (allowed, words, expected) in enumerate(test_cases):
        result = solution.countConsistentStrings(allowed, words)
        assert result == expected, f"Test case {i+1} failed: Expected {expected}, got {result}"

        result_optimized = solution.countConsistentStringsOptimized(allowed, words)
        assert result_optimized == expected, f"Optimized Test case {i+1} failed: Expected {expected}, got {result_optimized}"

    print("All test cases passed!")
