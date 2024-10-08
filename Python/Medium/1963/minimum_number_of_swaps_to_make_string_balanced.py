"""
1963. Minimum Number of Swaps to Make the String Balanced

Problem Statement:
You are given a 0-indexed string `s` of even length `n`. The string consists of exactly `n / 2` opening brackets '[' and `n / 2` closing brackets ']'.
A string is called balanced if and only if:
- It is the empty string, or
- It can be written as AB, where both A and B are balanced strings, or
- It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make `s` balanced.

Constraints:
- n == s.length
- 2 <= n <= 10^6
- n is even.
- s[i] is either '[' or ']'.
- The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.

Examples:

Example 1:
    Input: s = "][]["
    Output: 1
    Explanation: You can make the string balanced by swapping index 0 with index 3.
    The resulting string is "[[]]".

Example 2:
    Input: s = "]]][[["
    Output: 2
    Explanation: You can do the following to make the string balanced:
    - Swap index 0 with index 4. s = "[]][][".
    - Swap index 1 with index 5. s = "[[][]]".
    The resulting string is "[[][]]".

Example 3:
    Input: s = "[]"
    Output: 0
    Explanation: The string is already balanced.
"""

from collections import deque

class Solution:
    """
    This class implements a method to find the minimum number of swaps required to make a string of brackets balanced.
    """

    def minSwaps(self, s: str) -> int:
        """
        Finds the minimum number of swaps required to make the string balanced.
        
        Time Complexity: O(n), where n is the length of the string `s`.
        Space Complexity: O(n), due to the usage of the stack (deque).

        Args:
            s: str - The input string consisting of brackets.

        Returns:
            int - The minimum number of swaps required to balance the string.
        """
        stack = deque()
        unbalanced = 0

        for ch in s:
            if ch == "[":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()  # We found a matching opening bracket, so we remove it.
                else:
                    unbalanced += 1  # No matching opening bracket, so this is an unbalanced closing bracket.

        # The number of unbalanced brackets (extra closing ones) is halved, as each pair of swaps fixes two unbalanced brackets.
        return (unbalanced + 1) // 2


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ("][][", 1),
        ("]]][[[", 2),
        ("[]", 0),
        ("]][[][[", 1),
        ("]]]]]][[[[[[", 3),
    ]

    solution = Solution()

    for i, (s, expected) in enumerate(test_cases):
        result = solution.minSwaps(s)
        assert result == expected, f"Test case {i+1} failed: Expected {expected}, but got {result}"

    print("All test cases passed!")
