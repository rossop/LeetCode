"""
12. Integer to Roman

Problem Statement:
Given an integer, convert it to a Roman numeral.

Roman numerals are formed using the following symbols:
    I=1, V=5, X=10, L=50, C=100, D=500, M=1000

The subtraction rule applies for six cases:
    IV=4, IX=9, XL=40, XC=90, CD=400, CM=900

Constraints:
- 1 <= num <= 3999

Examples:

Example 1:
    Input: num = 3749
    Output: "MMMDCCXLIX"

Example 2:
    Input: num = 58
    Output: "LVIII"

Example 3:
    Input: num = 1994
    Output: "MCMXCIV"
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Converts an integer to a Roman numeral using a greedy while loop.

        Iterates over a list of (value, symbol) pairs in descending order.
        For each pair, repeatedly appends the symbol and subtracts the value
        while num >= value. The subtraction cases (IX, IV, etc.) are included
        as explicit entries so no special-casing is needed.

        Args:
            num (int): An integer in the range [1, 3999].

        Returns:
            str: The Roman numeral representation of num.

        Time complexity:  O(1) — the value range is fixed, so the number of
                          iterations is bounded by a constant.
        Space complexity: O(1)
        """
        vals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I"),
        ]

        result = ""
        for value, symbol in vals:
            while num >= value:
                result += symbol
                num -= value
        return result

    def intToRomanDivmod(self, num: int) -> str:
        """
        Converts an integer to a Roman numeral using divmod.

        Iterates over the same ordered value-symbol pairs. For each entry,
        divmod(num, val) returns (count, remainder) in one operation:
        - count  = how many times this symbol appears
        - num    = the remaining value to convert

        Appends symbol * count to avoid a nested while loop. The dict
        preserves insertion order (Python 3.7+), so descending order is
        maintained. Breaks early when num reaches 0.

        Args:
            num (int): An integer in the range [1, 3999].

        Returns:
            str: The Roman numeral representation of num.

        Time complexity:  O(1) — fixed iteration count.
        Space complexity: O(1)
        """
        roman_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C",  90: "XC",  50: "L",  40: "XL",
            10: "X",   9: "IX",   5: "V",   4: "IV", 1: "I",
        }

        result = []
        for val, symbol in roman_map.items():
            if num == 0:
                break
            count, num = divmod(num, val)
            result.append(symbol * count)

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (3749, "MMMDCCXLIX"),
        (58,   "LVIII"),
        (1994, "MCMXCIV"),
        (1,    "I"),
        (3999, "MMMCMXCIX"),
        (4,    "IV"),
        (9,    "IX"),
        (40,   "XL"),
        (400,  "CD"),
        (900,  "CM"),
    ]

    for label, method in [
        ("intToRoman      ", solution.intToRoman),
        ("intToRomanDivmod", solution.intToRomanDivmod),
    ]:
        for num, expected in test_cases:
            result = method(num)
            assert result == expected, \
                f"{label} failed on {num}: expected {expected!r}, got {result!r}"
        print(f"  {label} passed")

    print("All test cases passed!")
