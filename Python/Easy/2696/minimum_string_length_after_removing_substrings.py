"""
2696. Minimum String Length After Removing Substrings

Problem Statement:
You are given a string `s` consisting only of uppercase English letters.
You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from `s`.

Return the minimum possible length of the resulting string that you can obtain.

Constraints:
- 1 <= s.length <= 100
- `s` consists only of uppercase English letters.

Examples:

Example 1:
    Input: s = "ABFCACDB"
    Output: 2
    Explanation:
    We can do the following operations:
    - Remove "AB", resulting in "FCACDB".
    - Remove "CD", resulting in "FCAB".
    - Remove "AB", resulting in "FC".
    The minimum length of the resulting string is 2.

Example 2:
    Input: s = "ACBBD"
    Output: 5
    Explanation: No operation can be performed, so the string remains the same.
"""

from typing import List

class Solution:
    """
    This class implements two methods to find the minimum possible length of a string
    after removing all possible "AB" and "CD" substrings.
    
    Methods:
    1. minLength: Uses a stack-based approach to remove substrings.
    2. minLengthReplace: Uses string replacement until no more "AB" or "CD" are present.
    """

    def minLength(self, s: str) -> int:
        """
        Uses a stack to efficiently remove substrings "AB" and "CD" from the string.
        
        Time Complexity: O(n), where n is the length of the string `s`.
        Space Complexity: O(n), due to the space needed to store the stack.

        Args:
            s: str - The input string.

        Returns:
            int - The minimum possible length of the string after removal.
        """
        stack: List[str] = []

        for current_char in s:
            if not stack:
                stack.append(current_char)
                continue
            
            # Check if we can remove "AB" or "CD"
            if current_char == 'B' and stack[-1] == 'A':
                stack.pop()
            elif current_char == 'D' and stack[-1] == 'C':
                stack.pop()
            else:
                stack.append(current_char)
        
        # The remaining elements in the stack form the final string
        return len(stack)

    def minLengthReplace(self, s: str) -> int:
        """
        Uses string replacement to iteratively remove substrings "AB" and "CD" until none are left.
        
        Time Complexity: O(n^2) in the worst case, where n is the length of the string `s`, because each replacement operation may require scanning the entire string.
        Space Complexity: O(n), due to storing the string.

        Args:
            s: str - The input string.

        Returns:
            int - The minimum possible length of the string after removal.
        """
        while "AB" in s or "CD" in s:
            if "AB" in s:
                s = s.replace("AB", "")
            elif "CD" in s:
                s = s.replace("CD", "")

        return len(s)


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ("ABFCACDB", 2),
        ("ACBBD", 5),
        ("ABCDABCD", 0),
        ("A", 1),
        ("ABBACCDDA", 3),
    ]

    solution = Solution()

    # Test the stack-based method
    print("Testing minLength (Stack-based) method:")
    for i, (s, expected) in enumerate(test_cases):
        result = solution.minLength(s)
        assert result == expected, f"Test case {i+1} failed (Stack): Expected {expected}, but got {result}"
    print("All test cases passed for minLength (Stack-based) method!")

    # Test the replace-based method
    print("\nTesting minLengthReplace (String replacement) method:")
    for i, (s, expected) in enumerate(test_cases):
        result = solution.minLengthReplace(s)
        assert result == expected, f"Test case {i+1} failed (Replace): Expected {expected}, but got {result}"
    print("All test cases passed for minLengthReplace (String replacement) method!")
