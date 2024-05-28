class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A phrase is a palindrome if, after converting all uppercase letters
        into lowercas letters and removing all non-alphanumeric characters, it
        reads the same forward and backward. Alphanumeric characters include
        letters and numbers.

        Given a string s, return true if it is a palindrome, false otherwise.

        Examples:
            Example 1:
                Input: s = "A man, a plan, a canal: Panama"
                Output: True
                Explanation: "amanaplanacanalpanama" is a palindrome.

            Example 2:
                Input: s = "race a car"
                Output: False
                Explanation: "raceacar" is not a palindrome.

            Example 3:
                Input: s = " "
                Output: True
                Explanation: s is an empty string "" after removing
                    non-alphanumeric characters. Since an empty string reads
                    the same forward and backward, it is a palindrome.

        Args:
            s (str): The input string to check.

        Returns:
            bool: True if the input string is a palindrome, False otherwise.
        """
        # Remove non-alphanumeric chars and convert to lowercase using filter
        cleaned_s = ''.join(filter(str.isalnum, s)).lower()

        # Check if the cleaned string is a palindrome
        start = 0
        end = len(cleaned_s) - 1
        while start < end:
            if cleaned_s[start] != cleaned_s[end]:
                return False
            start += 1
            end -= 1
        return True


# Example usage:
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))  # Output: False
print(solution.isPalindrome(" "))  # Output: True
