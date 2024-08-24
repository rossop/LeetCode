"""
564. Find the Closest Palindrome
https://leetcode.com/problems/find-the-closest-palindrome/

Given a string n representing an integer, return the closest integer
(not including itself), which is a palindrome. If there is a tie,
return the smaller one.

The closest is defined as the absolute difference minimized between
two integers.
"""

from typing import List


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
        This method uses a two-pointer approach to convert the given number
        into a palindrome by mirroring the left half onto the right half.
        It then compares the resulting palindrome with potential smaller
        and larger palindromes to find the closest one.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Args:
            n (str): The input number as a string.

        Returns:
            str: The closest palindrome.
        """
        l: int = len(n)

        # Edge case for single-digit number
        if l == 1:
            return str(int(n) - 1)

        # Create the first mirrored palindrome
        nums: List[str] = list(n)
        left: int = 0
        right: int = l - 1

        while left < right:
            nums[right] = nums[left]
            left += 1
            right -= 1

        # Convert to a string and to an integer
        candidate = int("".join(nums))

        # Generate the possible candidates
        smaller_palindrome = self.adjust_palindrome(n, -1)
        larger_palindrome = self.adjust_palindrome(n, 1)

        # Convert candidate to integer
        num = int(n)

        # Check which is closest
        if candidate != num:
            candidates = [(abs(candidate - num), candidate),
                          (abs(smaller_palindrome - num), smaller_palindrome),
                          (abs(larger_palindrome - num), larger_palindrome)]
        else:
            candidates = [(abs(smaller_palindrome - num), smaller_palindrome),
                          (abs(larger_palindrome - num), larger_palindrome)]

        # Sort by difference, then by numeric value
        candidates.sort()

        return str(candidates[0][1])

    def adjust_palindrome(self, n: str, offset: int) -> int:
        """
        Generates the next palindrome by adjusting the middle part of the
        number and then mirroring it.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Args:
            n (str): The input number as a string.
            offset (int): The offset to adjust the middle of the number.

        Returns:
            int: The adjusted palindrome.
        """
        l: int = len(n)
        half: int = (l + 1) // 2
        left_half = str(int(n[:half]) + offset)

        # Mirror the left half
        if len(left_half) > half:
            palindrome = left_half + left_half[:-1][::-1]
        else:
            palindrome = left_half + left_half[:len(left_half) - (l % 2)][::-1]

        return int(palindrome)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("123", "121"),
        ("1", "0"),
        ("99", "101"),
        ("1001", "999"),
        ("12321", "12221"),
        ("998", "999"),
    ]

    for i, (k, expected) in enumerate(test_cases):
        result = solution.nearestPalindromic(k)
        assert result == expected, f"""
        Test case {i+1} failed: expected {expected}, got {result}"""

    print("All test cases passed!")
