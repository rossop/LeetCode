class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        Determines if 'typed' could be a result of a long press while typing 'name'.
        
        The function checks each character in 'typed' to ensure that it either matches
        the current character in 'name' or is a valid long press of the previous character.

        Time Complexity:
            O(n): The function iterates through the 'typed' string once, where `n` is the length of 'typed'.
        
        Space Complexity:
            O(1): The function uses a constant amount of extra space.

        Args:
            name (str): The original name string.
            typed (str): The string that was typed, possibly with long presses.

        Returns:
            bool: Returns True if 'typed' could be a result of a long press, otherwise False.
        """
        p1: int = 0
        p2: int = 0
        n: int = len(typed)
        m: int = len(name)

        while p2 < n:
            if p1 < m and name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            elif p2 > 0 and typed[p2] == typed[p2 - 1]:
                p2 += 1
            else:
                return False
        
        return p1 == m

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("alex", "aaleex", True),
        ("saeed", "ssaaedd", False),
        ("leelee", "lleeelee", True),
        ("laiden", "laiden", True),
        ("alex", "aaleexa", False),  # Additional test
        ("vtkgn", "vttkgnn", True)   # Additional test
    ]

    for i, (name, typed, expected) in enumerate(test_cases):
        result = solution.isLongPressedName(name, typed)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases passed!")