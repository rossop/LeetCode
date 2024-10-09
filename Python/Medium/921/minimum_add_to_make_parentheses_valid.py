"""
921. Minimum Add to Make Parentheses Valid

Problem Statement:
A parentheses string is valid if and only if:
- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.
Return the minimum number of moves required to make `s` valid.

Constraints:
- 1 <= s.length <= 1000
- `s[i]` is either '(' or ')'.

Examples:

Example 1:
    Input: s = "())"
    Output: 1

Example 2:
    Input: s = "((("
    Output: 3
"""

from typing import List

class Solution:
    """
    This class implements two methods to find the minimum number of moves required to make the parentheses string valid.
    
    Methods:
    1. minAddToMakeValid: Uses a stack to track unmatched parentheses.
    2. minAddToMakeValidCounter: Optimized version that uses counters to reduce space complexity.
    """

    def minAddToMakeValid(self, s: str) -> int:
        """
        Uses a stack to track unmatched parentheses.
        Each unmatched closing parenthesis increases a counter, and each unmatched opening parenthesis is added to the stack.
        
        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(n), due to the space required by the stack.
        
        Args:
            s: str - The input string consisting of parentheses.

        Returns:
            int - The minimum number of moves required to make the string valid.
        """
        stack: List[str] = []
        counter: int = 0

        for par in s:
            if par == '(':
                stack.append(par)
            if par == ')':
                if stack:
                    stack.pop()  # We found a matching opening parenthesis, so we remove it.
                else:
                    counter += 1  # No matching opening parenthesis, so we increase the counter.

        # Return the sum of unmatched closing parentheses (counter) and unmatched opening parentheses (len(stack)).
        return counter + len(stack)

    def minAddToMakeValidCounter(self, s: str) -> int:
        """
        Optimizes the stack-based approach by using two counters to track unmatched opening and closing parentheses.
        This reduces space complexity while maintaining the same logic as the stack-based solution.
        
        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(1), as we are only using two counters.

        Args:
            s: str - The input string consisting of parentheses.

        Returns:
            int - The minimum number of moves required to make the string valid.
        """
        open_brackets: int = 0
        unmatched_counter: int = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1  # Found a matching open parenthesis.
                else:
                    unmatched_counter += 1  # Unmatched closing parenthesis.

        # The total number of unmatched parentheses is the sum of unmatched opening and closing parentheses.
        return open_brackets + unmatched_counter


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ("())", 1),  # Need one more opening parenthesis.
        ("(((", 3),  # Need three more closing parentheses.
        ("()", 0),   # Already valid.
        ("()()", 0), # Already valid.
        ("))((", 4), # Need two opening and two closing parentheses.
    ]

    solution = Solution()

    # Test the stack-based method
    print("Testing minAddToMakeValid (Stack-based) method:")
    for i, (s, expected) in enumerate(test_cases):
        result = solution.minAddToMakeValid(s)
        assert result == expected, f"Test case {i+1} failed (Stack): Expected {expected}, but got {result}"
    print("All test cases passed for minAddToMakeValid (Stack-based) method!")

    # Test the counter-based method
    print("\nTesting minAddToMakeValidCounter (Counter-based) method:")
    for i, (s, expected) in enumerate(test_cases):
        result = solution.minAddToMakeValidCounter(s)
        assert result == expected, f"Test case {i+1} failed (Counter): Expected {expected}, but got {result}"
    print("All test cases passed for minAddToMakeValidCounter (Counter-based) method!")
