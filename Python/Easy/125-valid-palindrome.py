class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if the given string is a palindrome by first filtering out non-alphanumeric 
        characters and then checking if the resulting string is the same when read forwards and backwards.

        This method uses a two-pointer technique after filtering the string. The filtering step 
        uses a list comprehension to create a new list of characters, which increases space usage.

        Args:
            s (str): The input string to be checked for being a palindrome.

        Returns:
            bool: True if the string is a palindrome, False otherwise.

        Time Complexity:
            O(n): The string is processed once to filter non-alphanumeric characters and once to check palindrome.

        Space Complexity:
            O(n): An additional list is created to store the filtered characters.

        Example:
            Input: s = "A man, a plan, a canal: Panama"
            Output: True
        
        Constraints:
            - 1 <= s.length <= 2 * 10^5
            - s consists only of printable ASCII characters.
        """
        s = [char.lower() for char in s if char.isalnum()]
        n = len(s)
        L: int = 0
        R: int = n - 1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True

    def isPalindromeOptimized(self, s: str) -> bool:
        """
        Determines if the given string is a palindrome by using a two-pointer technique directly 
        on the original string, skipping non-alphanumeric characters during the comparison.

        This method avoids creating additional space by directly comparing characters 
        from both ends, moving pointers inward, and skipping non-alphanumeric characters.

        Args:
            s (str): The input string to be checked for being a palindrome.

        Returns:
            bool: True if the string is a palindrome, False otherwise.

        Time Complexity:
            O(n): The string is processed once with two pointers.

        Space Complexity:
            O(1): No additional space is required other than a few variables.

        Example:
            Input: s = "A man, a plan, a canal: Panama"
            Output: True
        
        Comparison with the First Method:
            - Both methods have O(n) time complexity.
            - The first method has O(n) space complexity due to the filtered list, whereas the optimized method has O(1) space complexity.
            - The optimized method is preferable when space efficiency is crucial.

        Constraints:
            - 1 <= s.length <= 2 * 10^5
            - s consists only of printable ASCII characters.
        """
        n = len(s)
        L: int = 0
        R: int = n - 1
        while L < R:
            if not s[L].isalnum():
                L += 1
                continue
            
            if not s[R].isalnum():
                R -= 1
                continue

            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        return True


    def isPalindromeFilter(self, s: str) -> bool:
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


if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases and their expected outputs
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("No lemon, no melon", True),
        ("Was it a car or a cat I saw?", True),
    ]

    # Run and validate the test cases
    for i, (input_str, expected) in enumerate(test_cases):
        result = solution.isPalindrome(input_str)
        assert result == expected, f"Test case {i+1} failed for isPalindrome: expected {expected}, got {result}"

        result_optimized = solution.isPalindromeOptimized(input_str)
        assert result_optimized == expected, f"Test case {i+1} failed for isPalindromeOptimized: expected {expected}, got {result_optimized}"
        
        result_optimized = solution.isPalindromeFilter(input_str)
        assert result_optimized == expected, f"Test case {i+1} failed for isPalindromeFilter: expected {expected}, got {result_optimized}"

    print("All test cases passed!")