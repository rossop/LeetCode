"""
13. Roman to Integer

Problem Statement:
Roman numerals are represented by seven symbols: I=1, V=5, X=10, L=50, C=100,
D=500, M=1000. Numerals are written largest to smallest left to right, except
in six subtraction cases: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900.

Given a Roman numeral string s, convert it to an integer.

Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
- It is guaranteed that s is a valid Roman numeral in the range [1, 3999]

Examples:

Example 1:
    Input: s = "III"
    Output: 3

Example 2:
    Input: s = "LVIII"
    Output: 58

Example 3:
    Input: s = "MCMXCIV"
    Output: 1994
"""

from typing import Dict


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.

        The function uses a dictionary to map Roman numeral symbols to their integer values. It then iterates through the input string, `s`, and sums the corresponding integer values. If a smaller value precedes a larger value (indicating subtraction, such as in "IV" for 4), the function subtracts the smaller value from the larger value.

        Args:
        -----
        s : str
            A string representing a Roman numeral. The string is guaranteed to be a valid Roman numeral within the range [1, 3999].
        
        Returns:
        --------
        int
            The integer value corresponding to the Roman numeral.

        Example:
        --------
        >>> solution = Solution()
        >>> solution.romanToInt("III")
        3
        >>> solution.romanToInt("LVIII")
        58
        >>> solution.romanToInt("MCMXCIV")
        1994

        Time Complexity:
        ---------------
        O(n), where n is the length of the input string `s`. The function processes each character in the string exactly once.

        Space Complexity:
        ----------------
        O(1), as the function uses a fixed amount of additional space (a dictionary and a few integer variables), regardless of the input size.
        """
        d: Dict[str, int] = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        }
        summ: int = 0
        n = len(s)
        i = 0

        while i < n:
            if i + 1 < n and d[s[i]] < d[s[i + 1]]:
                summ += (d[s[i + 1]] - d[s[i]])
                i += 2
            else:
                summ += d[s[i]]
                i += 1

        return summ

    def romanToIntReversed(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer by iterating in reverse.

        Iterates right to left using reversed(), tracking the previous value.
        If the current symbol is smaller than the one to its right (prev_val),
        it is a subtraction case and is subtracted; otherwise it is added.

        Avoids the index peek (s[i+1]) needed in the forward pass — the
        previous value from the last iteration serves the same purpose.
        reversed() iterates in O(1) extra space with no string reversal.

        Args:
            s (str): A valid Roman numeral string in the range [1, 3999].

        Returns:
            int: The integer value of the Roman numeral.

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
        }

        ans = 0
        prev_val = 0

        for char in reversed(s):
            curr_val = roman_map[char]
            if curr_val < prev_val:
                ans -= curr_val
            else:
                ans += curr_val
            prev_val = curr_val

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("MMMCMXCIX", 3999),
    ]

    for label, method in [
        ("romanToInt        ", solution.romanToInt),
        ("romanToIntReversed", solution.romanToIntReversed),
    ]:
        for s, expected in test_cases:
            result = method(s)
            assert result == expected, \
                f"{label} failed on {s!r}: expected {expected}, got {result}"
        print(f"  {label} passed")

    print("All test cases passed!")