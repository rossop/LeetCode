from typing import Dict
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if t is an anagram of s using a custom counting method.

        This method manually counts the occurrences of each character in both strings
        and compares these counts to determine if the strings are anagrams.

        Time Complexity:
            O(n): Where n is the length of the strings.
        
        Space Complexity:
            O(1): The space used by the custom counter is proportional to the number of 
            unique characters in the strings. Since there are only 26 possible lowercase 
            English letters, this is considered O(1) space.

        Args:
            s (str): The original string.
            t (str): The string to check if it's an anagram of s.

        Returns:
            bool: True if t is an anagram of s, otherwise False.
        """
        if len(s) != len(t):
            return False
        
        def count(string: str) -> Dict[str, int]:
            sCount: Dict[str, int] = {}

            for c in string:
                if c in sCount:
                    sCount[c] += 1
                else:
                    sCount[c] = 1
            
            return sCount
        
        sCount: Dict[str, int] = count(s)
        tCount: Dict[str, int] = count(t)

        return sCount == tCount

    def isAnagramCounter(self, s: str, t: str) -> bool:
        """
        Determines if t is an anagram of s using the Counter class from collections.

        This method uses the Counter class to count the occurrences of each character
        in both strings and compares these counts.

        Time Complexity:
            O(n): Where n is the length of the strings.
        
        Space Complexity:
            O(1): The space used by the Counter is proportional to the number of 
            unique characters in the strings. Since there are only 26 possible lowercase 
            English letters, this is considered O(1) space.

        Args:
            s (str): The original string.
            t (str): The string to check if it's an anagram of s.

        Returns:
            bool: True if t is an anagram of s, otherwise False.
        """
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
        ("a", "a", True),
        ("ab", "ba", True),
        ("abc", "cba", True),
        ("abc", "abcd", False)
    ]

    for i, (s, t, expected) in enumerate(test_cases):
        result_custom: bool = solution.isAnagram(s, t)
        result_counter: bool = solution.isAnagramCounter(s, t)
        assert result_custom == expected, f"Test case {i+1} failed for custom solution: expected {expected}, got {result_custom}"
        assert result_counter == expected, f"Test case {i+1} failed for Counter solution: expected {expected}, got {result_counter}"

    print("All test cases passed!")