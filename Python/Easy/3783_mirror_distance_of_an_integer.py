"""
3783. Mirror Distance of an Integer

Problem Statement:
You are given an integer n. Define its mirror distance as abs(n - reverse(n))
where reverse(n) is the integer formed by reversing the digits of n.

Return the mirror distance of n.

Constraints:
- 1 <= n <= 10^9

Examples:

Example 1:
    Input: n = 25
    Output: 27
    Explanation: reverse(25) = 52. abs(25 - 52) = 27.

Example 2:
    Input: n = 10
    Output: 9
    Explanation: reverse(10) = 01 = 1. abs(10 - 1) = 9.

Example 3:
    Input: n = 7
    Output: 0
    Explanation: reverse(7) = 7. abs(7 - 7) = 0.
"""


class Solution:
    def mirrorDistance(self, n: int) -> int:
        """
        Returns the mirror distance of n, defined as abs(n - reverse(n)).

        Reverses the digits of n by converting to string and slicing, which
        handles leading zeros automatically (e.g. reverse(10) = "01" → 1).
        Returns the absolute difference between n and its digit-reversed form.

        Args:
            n (int): The input integer.

        Returns:
            int: The absolute difference between n and reverse(n).

        Time Complexity:
            O(d) where d = number of digits in n, i.e. O(log n).

        Space Complexity:
            O(d): The string representation of n.
        """
        def reverse(n: int) -> int:
            return int(str(n)[::-1])

        return abs(reverse(n) - n)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (25, 27),
        (10, 9),
        (7, 0),
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        result = solution.mirrorDistance(n)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed")

    print("All test cases passed!")
