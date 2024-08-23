"""
592. Fraction Addition and Subtraction

Given a string expression representing an expression of fraction addition
and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is
an integer, change it to the format of a fraction that has a denominator 1.
So in this case, 2 should be converted to 2/1.

Problem Link: https://leetcode.com/problems/fraction-addition-and-subtraction/

Examples:
    Example 1:
        Input: expression = "-1/2+1/2"
        Output: "0/1"
        
    Example 2:
        Input: expression = "-1/2+1/2+1/3"
        Output: "1/3"
        
    Example 3:
        Input: expression = "1/3-1/2"
        Output: "-1/6"

Constraints:
    The input string only contains '0' to '9', '/', '+' and '-'.
    Each fraction (input and output) has the format ±numerator/denominator.
    The numerator and denominator of each fraction will always be in the range
        [1, 10].
    The number of given fractions will be in the range [1, 10].
    The numerator and denominator of the final result are guaranteed to be
    valid and in the range of 32-bit int.

This script contains a Solution class with two methods to solve the problem:
- `fractionAddition`: The original approach to calculate the result.
- `fractionAdditionOptimized`: An optimized approach with dynamic denominator
    adjustment.

Both methods have been tested with multiple test cases.
"""
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        """
        Approach:
        This method computes the result of adding or subtracting a sequence
        of fractions.
        It handles fractions by adjusting the common denominator dynamically
        and then reducing the fraction using the GCD.

        Time Complexity:
            O(n): We process each character in the string exactly once.

        Space Complexity:
            O(n): We store the expression and manipulate it, leading to O(n)
            space usage.

        Args:
            expression (str): A string representing a mathematical expression
            of fractions.

        Returns:
            str: The result of the expression as an irreducible fraction in
            string format.
        """
        numerator: int = 0
        denominator: int = 1

        # Ensure the first character is a sign
        if expression[0].isdigit():
            expression = '+' + expression

        i: int = 0
        expr_length: int = len(expression)

        while i < expr_length:
            sign: int = -1 if expression[i] == '-' else 1
            i += 1

            j: int = i
            while j < expr_length and expression[j] not in "+-":
                j += 1

            numerator_str, denominator_str = expression[i:j].split('/')
            current_numerator: int = sign * int(numerator_str)
            current_denominator: int = int(denominator_str)

            numerator = numerator * current_denominator + \
                current_numerator * denominator
            denominator *= current_denominator

            common_divisor: int = gcd(abs(numerator), denominator)
            numerator //= common_divisor
            denominator //= common_divisor

            i = j

        return f'{numerator}/{denominator}'

    def fractionAdditionOptimized(self, expression: str) -> str:
        """
        Optimized Approach:
        This method computes the result of adding or subtracting a sequence of
        fractions in a more direct and dynamic manner. It maintains a running
        total and adjusts the denominator dynamically.

        Time Complexity:
            O(n): Each fraction is processed as we iterate through the
            expression.

        Space Complexity:
            O(n): The space is used to store the result and process the string.

        Args:
            expression (str): A string representing a mathematical expression
            of fractions.

        Returns:
            str: The result of the expression as an irreducible fraction in
            string format.
        """
        numerator, denominator = 0, 1

        i, n = 0, len(expression)
        while i < n:
            sign = 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1

            j = i
            while j < n and expression[j] != '/' and expression[j] not in "+-":
                j += 1
            numerator_part = sign * int(expression[i:j])

            i = j + 1
            j = i
            while j < n and expression[j] not in "+-":
                j += 1
            denominator_part = int(expression[i:j])

            numerator = numerator * denominator_part + \
                numerator_part * denominator
            denominator *= denominator_part

            g = gcd(abs(numerator), denominator)
            numerator //= g
            denominator //= g

            i = j

        return f"{numerator}/{denominator}"

    # In case I cannot use math.gcd
    @classmethod
    def findGCD(x: int, y: int) -> int:
        """
        Find the Greatest Common Divisor (GCD) of two integers using the
        iterative form of the Euclidean algorithm.

        This implementation iteratively reduces the problem by replacing
        the larger number with the remainder when the larger number is
        divided by the smaller number. The process continues until the
        remainder is zero, at which point the GCD is found.

        Time Complexity:
            O(log(min(x, y))): The number of iterations is proportional to
            the logarithm of the smaller of the two input numbers.

        Space Complexity:
            O(1): The algorithm uses a constant amount of space, regardless
            of the size of the input numbers.

        Args:
            x (int): The first integer.
            y (int): The second integer.

        Returns:
            int: The GCD of x and y.
        """
        curr: int = x
        div: int = y

        while div > 0:
            curr, div = div, curr % div

        return curr


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("-1/2+1/2", "0/1"),
        ("-1/2+1/2+1/3", "1/3"),
        ("1/3-1/2", "-1/6"),
        ("5/3+1/3", "2/1"),
        ("2/4-1/4", "1/4"),
    ]

    for expr, expected in test_cases:
        result = solution.fractionAddition(expr)
        assert result == expected, f"""
            Test case failed for {expr}.
            Expected {expected}, got {result}"""
        result_optimized = solution.fractionAdditionOptimized(expr)
        assert result_optimized == expected, f"""
            Test case failed for {expr}.
            Expected {expected}, got {result_optimized}"""

    print("All test cases passed!")
