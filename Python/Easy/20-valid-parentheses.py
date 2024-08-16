"""
20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

This file contains a solution to the "Valid Parentheses" problem. The solution is implemented 
in the `Solution` class, which provides a method to determine if a given string of parentheses 
is valid. The method uses a stack-based approach to ensure that each opening bracket has a 
corresponding and correctly ordered closing bracket.
"""

from typing import List, Dict

class Solution:
    """
    Solution class for the "Valid Parentheses" problem.

    This class provides a method to check whether a given string containing 
    parentheses is valid according to the following criteria:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.

    The solution uses a stack-based approach to validate the string.
    """

    def isValid(self, s: str) -> bool:
        """
        Determines if the input string of parentheses is valid.

        The method uses a stack to keep track of opening brackets. For each 
        closing bracket, it checks whether it matches the most recent opening 
        bracket on the stack. If all brackets are correctly matched, the string 
        is considered valid.

        Time Complexity: O(n) where n is the length of the input string.
        Space Complexity: O(n) in the worst case if all brackets are opening brackets.

        Args:
            s (str): The input string containing the parentheses.

        Returns:
            bool: True if the string is valid, False otherwise.
        """
        if len(s) % 2 != 0:
            return False
        
        stack: List[str] = []
        parens: Dict[str, str] = {
            ')': '(', 
            '}': '{', 
            ']': '[',
        }

        for c in s:
            if c in parens.values():
                stack.append(c)
            else:
                if (len(stack) > 0) and (parens[c] == stack[-1]):
                    _ = stack.pop()
                else:
                    return False
        
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("()", True),          # Example 1: Simple valid case
        ("()[]{}", True),      # Example 2: Multiple types of valid brackets
        ("(]", False),         # Example 3: Invalid due to mismatched brackets
        ("([{}])", True),      # Additional case: Nested valid brackets
        ("([)]", False),       # Additional case: Nested invalid brackets
        ("{[()]}", True),      # Additional case: Complex valid case
        ("", True),            # Edge case: Empty string is valid
        ("{", False),          # Edge case: Single opening bracket
        ("}", False),          # Edge case: Single closing bracket
        ("[({})", False)       # Edge case: Unmatched opening bracket
    ]

    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = solution.isValid(input_str)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")