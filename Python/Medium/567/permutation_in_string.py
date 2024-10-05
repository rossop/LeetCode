"""
567. Permutation in String

Problem Statement:
Given two strings `s1` and `s2`, return true if `s2` contains a permutation of `s1`, or false otherwise.
In other words, return true if one of `s1`'s permutations is a substring of `s2`.

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.

Examples:

Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: False
"""

from typing import List, Dict
from collections import Counter

class Solution:
    """
    This class provides two methods to check if one string is a permutation of a substring of another string.
    
    Methods:
    1. checkInclusion: Uses frequency arrays for efficient checking of character counts.
    2. checkInclusionWindow: Uses sliding window and dictionary counters for dynamic tracking.
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Uses frequency arrays to check if any permutation of `s1` is a substring of `s2`.
        
        Time Complexity: O(n2), where n2 is the length of `s2`.
        Space Complexity: O(1), as the size of the frequency arrays is constant (26 for lowercase letters).
        
        Args:
            s1: str - The first string (permutation to check).
            s2: str - The second string (contains substring to check against).
        
        Returns:
            bool - True if any permutation of `s1` is a substring of `s2`, otherwise False.
        """
        n1: int = len(s1)
        n2: int = len(s2)

        # If s1 is longer than s2, it's impossible for any permutation of s1 to be in s2
        if n1 > n2:
            return False

        # Initialize frequency counts for both s1 and s2 (the first n1 characters)
        s1_counts: List[int] = [0] * 26
        s2_counts: List[int] = [0] * 26

        # Fill in the frequency counts for the first n1 characters
        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1

        # Check if the frequency counts match
        if s1_counts == s2_counts:
            return True

        # Slide the window across s2, updating the frequency counts
        for i in range(n1, n2):
            s2_counts[ord(s2[i]) - 97] += 1  # Add the new character to the window
            s2_counts[ord(s2[i - n1]) - ord('a')] -= 1  # Remove the character that's sliding out
            if s1_counts == s2_counts:
                return True

        return False

    def checkInclusionWindow(self, s1: str, s2: str) -> bool:
        """
        Uses sliding window and dictionary counters to check if any permutation of `s1` is a substring of `s2`.
        
        Time Complexity: O(n2), where n2 is the length of `s2`.
        Space Complexity: O(n1), where n1 is the length of `s1`.
        
        Args:
            s1: str - The first string (permutation to check).
            s2: str - The second string (contains substring to check against).
        
        Returns:
            bool - True if any permutation of `s1` is a substring of `s2`, otherwise False.
        """
        if len(s1) == 0:
            return False

        s1_count: Dict[str, int] = Counter(s1)  # Count frequency of characters in s1
        chars_len: int = len(s1)

        # Initialize window count with first `chars_len - 1` characters of s2
        left: int = 0
        window_count: Dict[str, int] = Counter(s2[:chars_len - 1])

        # Slide the window over `s2` and compare counts
        for right in range(chars_len - 1, len(s2)):
            # Add the new character to the window
            window_count[s2[right]] += 1
            
            # Check if the window matches s1's permutation
            if window_count == s1_count:
                return True
            
            # Remove the character that's sliding out from the left of the window
            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]
            left += 1

        return False


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("adc", "dcda", True),
        ("hello", "ooolleoooleh", False),
    ]

    solution = Solution()

    # Test the checkInclusion method
    print("Testing checkInclusion method:")
    for i, (s1, s2, expected) in enumerate(test_cases):
        result = solution.checkInclusion(s1, s2)
        assert result == expected, f"Test case {i+1} failed (checkInclusion): Expected {expected}, but got {result}"
    print("All test cases passed for checkInclusion method!")

    # Test the checkInclusionWindow method
    print("\nTesting checkInclusionWindow method:")
    for i, (s1, s2, expected) in enumerate(test_cases):
        result = solution.checkInclusionWindow(s1, s2)
        assert result == expected, f"Test case {i+1} failed (checkInclusionWindow): Expected {expected}, but got {result}"
    print("All test cases passed for checkInclusionWindow method!")