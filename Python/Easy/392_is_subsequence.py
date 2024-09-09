class Solution:
    """
    A class to determine if one string is a subsequence of another.

    This class provides a method to check whether a given string `s` is a subsequence
    of another string `t`. A subsequence of a string is a new string that is formed
    from the original string by deleting some (can be none) of the characters without 
    disturbing the relative positions of the remaining characters.

    Example Usage:
        solution = Solution()
        result = solution.isSubsequence("abc", "ahbgdc")
        print(result)  # Output: True

    Methods:
        isSubsequence(s: str, t: str) -> bool:
            Determines whether string `s` is a subsequence of string `t`.
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Determines if the string `s` is a subsequence of the string `t`.

        A subsequence is defined as a sequence derived from another sequence 
        by deleting some or no elements without changing the order of the 
        remaining elements.

        Args:
            s (str): The string to check as a subsequence.
            t (str): The target string in which to check for the subsequence.

        Returns:
            bool: True if `s` is a subsequence of `t`, False otherwise.

        Example:
            >>> solution = Solution()
            >>> solution.isSubsequence("abc", "ahbgdc")
            True
            >>> solution.isSubsequence("axc", "ahbgdc")
            False

        Time Complexity:
            O(m), where m is the length of `t`. The function processes each 
            character in the string `t` exactly once.

        Space Complexity:
            O(1), as the function uses a constant amount of space.

        Notes:
            We only get to the end of list 's' if all of 's' is in 't'.
        """
        a, b = 0, 0
        n, m = len(s), len(t)
        
        while a < n and b < m:
            if s[a] == t[b]:
                a += 1
            b += 1
            
        return a == n

    def isSubsequenceAlternative(self, s: str, t: str) -> bool:
        """
        An alternative method to determine if the string `s` is a subsequence of the string `t`.

        This method iterates through the target string `t` and attempts to match characters
        from the string `s`. If all characters in `s` are found in `t` in order, it returns True.

        Args:
            s (str): The string to check as a subsequence.
            t (str): The target string in which to check for the subsequence.

        Returns:
            bool: True if `s` is a subsequence of `t`, False otherwise.

        Example:
            >>> solution = Solution()
            >>> solution.isSubsequenceAlternative("abc", "ahbgdc")
            True
            >>> solution.isSubsequenceAlternative("axc", "ahbgdc")
            False

        Time Complexity:
            O(T), where T is the length of `t`. The function processes each character 
            in the string `t` exactly once.

        Space Complexity:
            O(1), as the function uses a constant amount of space.
        """
        S = len(s)
        T = len(t)
        if s == '': 
            return True
        if S > T: 
            return False

        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S - 1:
                    return True
                j += 1
        
        return False


if __name__ == "__main__":
    # Define the test cases as a list of tuples
    test_cases = [
        ("abc", "ahbgdc", True, "Method 1, Test case 1 failed"),
        ("axc", "ahbgdc", False, "Method 1, Test case 2 failed"),
        ("", "ahbgdc", True, "Method 1, Test case 3 failed"),
        ("abc", "", False, "Method 1, Test case 4 failed"),
        ("ahbgdc", "ahbgdc", True, "Method 1, Test case 5 failed"),
    ]

    # Instantiate the solution class
    solution = Solution()

    # Loop through the test cases and check for both methods
    for s, t, expected, error_msg in test_cases:
        assert solution.isSubsequence(s, t) == expected, error_msg
        assert solution.isSubsequenceAlternative(s, t) == expected, error_msg.replace("Method 1", "Method 2")

    print("All test cases passed!")