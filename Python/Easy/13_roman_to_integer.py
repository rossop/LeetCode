class Solution:
    """
    A class to convert Roman numerals to their corresponding integer values.

    Roman numerals are a numeral system that originated in ancient Rome and remained the usual way of writing numbers throughout Europe well into the Late Middle Ages. They are based on seven symbols:
    
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    
    Roman numerals are usually written from largest to smallest from left to right. However, some numerals require subtraction (e.g., IV for 4 and IX for 9). The subtraction rule applies in the following cases:
    
    - 'I' can precede 'V' (5) and 'X' (10) to make 4 and 9.
    - 'X' can precede 'L' (50) and 'C' (100) to make 40 and 90.
    - 'C' can precede 'D' (500) and 'M' (1000) to make 400 and 900.
    
    This class provides a method to convert any valid Roman numeral (within the range [1, 3999]) into its integer representation.

    Methods
    -------
    romanToInt(s: str) -> int
        Converts a Roman numeral string to an integer.
    """

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


if __name__ == "__main__":
    # Test cases with assertions
    solution = Solution()
    
    assert solution.romanToInt("III") == 3, "Test case 1 failed"
    assert solution.romanToInt("IV") == 4, "Test case 2 failed"
    assert solution.romanToInt("IX") == 9, "Test case 3 failed"
    assert solution.romanToInt("LVIII") == 58, "Test case 4 failed"
    assert solution.romanToInt("MCMXCIV") == 1994, "Test case 5 failed"
    assert solution.romanToInt("MMMCMXCIX") == 3999, "Test case 6 failed"  # Maximum value

    print("All test cases passed!")