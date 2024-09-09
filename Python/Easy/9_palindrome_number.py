class PalindromeNumber:
    """
    9. Palindrome Number
    https://leetcode.com/problems/palindrome-number

    Class to solve the problem of determining if an integer is a palindrome.

    A palindrome is a number that reads the same backward as forward. For example, 121 is a palindrome 
    while -121 is not.

    This class provides three methods to check whether a given integer is a palindrome:
    1. Without converting the integer to a string (`isPalindromeNoString`).
    2. Using two pointers after converting the integer to a string (`isPalindromePointers`).
    3. By reversing the string representation of the integer (`isPalindromeConvertingToString`).
    """

    def isPalindromeNoString(self, x: int) -> bool:
        """
        Checks if a number is a palindrome without converting it to a string.

        This method uses a mathematical approach by comparing the digits of the number from the front and back.

        Time Complexity: O(log10(n))
        Space Complexity: O(1)

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if the integer is a palindrome, False otherwise.
        """
        if x < 0:
            return False
        
        div: int = 1
        while x >= 10 * div:
            div *= 10

        while x:
            if x // div != x % 10: # compare rightmost digit  to left most digit
                return False
            x = (x % div) // 10
            div //= 100
        return True

    def isPalindromePointers(self, x: int) -> bool:
        """
        Checks if a number is a palindrome using two pointers after converting it to a string.

        The method compares characters from the start and end of the string representation of the number, moving inward.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if the integer is a palindrome, False otherwise.
        """
        if x < 0:
            return False
        
        num: str = str(x)
        L: int = 0
        R: int = len(num) - 1
        while L < R:
            if num[L] != num[R]:
                return False
            L += 1
            R -= 1
        return True

    def isPalindromeConvertingToString(self, x: int) -> bool:
        """
        Checks if a number is a palindrome by reversing its string representation.

        The method converts the integer to a string, reverses the string, and compares it to the original.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if the integer is a palindrome, False otherwise.
        """
        if x < 0:
            return False

        return x == int(str(x)[::-1])


if __name__ == "__main__":
    solution = PalindromeNumber()

    # Test cases
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (12321, True),
        (0, True),
        (1234321, True),
        (-101, False),
        (1, True),
    ]

    for i, (x, expected) in enumerate(test_cases):
        assert solution.isPalindromeNoString(x) == expected, f"Test case {i+1} failed for isPalindromeNoString: expected {expected}, got {solution.isPalindromeNoString(x)}"
        assert solution.isPalindromePointers(x) == expected, f"Test case {i+1} failed for isPalindromePointers: expected {expected}, got {solution.isPalindromePointers(x)}"
        assert solution.isPalindromeConvertingToString(x) == expected, f"Test case {i+1} failed for isPalindromeConvertingToString: expected {expected}, got {solution.isPalindromeConvertingToString(x)}"

    print("All test cases passed!")