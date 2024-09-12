"""
1071. Greatest Common Divisor of Strings

Problem Statement:
For two strings `s` and `t`, we say "t divides s" if and only if 
`s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or 
more times).

Given two strings str1 and str2, return the largest string `x` such that `x` 
divides both str1 and str2.

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of uppercase English letters.

Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

"""

from math import gcd
from typing import List

class Solution:
    """
    Solution class for finding the greatest common divisor (GCD) of two strings.
    """

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Method 1: Uses the greatest common divisor (GCD) of the string lengths 
        to determine the largest string that can divide both `str1` and `str2`.

        The approach checks if concatenating the strings in reverse order 
        results in the same string (i.e., `str1 + str2 == str2 + str1`). 
        If not, return an empty string.

        Time Complexity:
            O(n + m), where n and m are the lengths of str1 and str2, respectively.
        
        Space Complexity:
            O(1), as we are using only a few extra variables, not proportional 
            to the input size.
        
        Args:
            str1: The first string.
            str2: The second string.

        Returns:
            The greatest common divisor of the two strings if they exist, 
            otherwise an empty string.
        """
        # Check if they have a common divisor
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]

    def gcdOfStringsIterative(self, str1: str, str2: str) -> str:
        """
        Method 2: Iterative approach to find the greatest common divisor 
        of the two strings. This approach builds the common prefix and ensures 
        it divides both strings properly.

        Time Complexity:
            O(n * min(m,n)), where n and m are the lengths of str1 and str2, 
            respectively.
        
        Space Complexity:
            O(n), where n is the length of the common divisor string.
        
        Args:
            str1: The first string.
            str2: The second string.

        Returns:
            The greatest common divisor string if one exists, otherwise an 
            empty string.
        """
        min_len = min(len(str1), len(str2))
        gcd_str = ""

        # Check each prefix of the minimum length string
        for i in range(1, min_len + 1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                prefix = str1[:i]
                if str1 == prefix * (len(str1) // i) and str2 == prefix * (len(str2) // i):
                    gcd_str = prefix
        
        return gcd_str

    def gcdOfStringsOptimized(self, str1: str, str2: str) -> str:
        """
        Optimized method that directly checks for divisibility without building 
        intermediate results.

        Time Complexity:
            O(min(n, m)), where n and m are the lengths of str1 and str2, respectively.
        
        Space Complexity:
            O(1), as we are using constant extra space.
        
        Args:
            str1: The first string.
            str2: The second string.

        Returns:
            The greatest common divisor string if one exists, otherwise an 
            empty string.
        """
        # If the concatenation of both strings in reverse order isn't equal, return ""
        if str1 + str2 != str2 + str1:
            return ""
        
        # Directly return the greatest common divisor of the string lengths
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("ABCABC", "ABC", "ABC"),    # Example 1
        ("ABABAB", "ABAB", "AB"),    # Example 2
        ("LEET", "CODE", ""),        # Example 3
        ("AAAA", "AA", "AA"),        # Custom Test Case 1
        ("XYZXYZ", "XYZ", "XYZ"),    # Custom Test Case 2
    ]

    # Instantiate the solution class
    solution = Solution()

    # Test the methods
    for i, (str1, str2, expected) in enumerate(test_cases):
        result1 = solution.gcdOfStrings(str1, str2)
        assert result1 == expected, f"Method 1 failed for test case {i+1}: Expected {expected}, got {result1}"

        result2 = solution.gcdOfStringsIterative(str1, str2)
        assert result2 == expected, f"Method 2 failed for test case {i+1}: Expected {expected}, got {result2}"

        result3 = solution.gcdOfStringsOptimized(str1, str2)
        assert result3 == expected, f"Optimized Method failed for test case {i+1}: Expected {expected}, got {result3}"

    print("All test cases passed!")
