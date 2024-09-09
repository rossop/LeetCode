from typing import Dict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determines if the ransomNote can be constructed using the letters from the magazine.
        
        This function uses a dictionary to count the occurrences of each character in the magazine,
        then iterates through the ransomNote to check if each character can be "used" from the magazine.
        If a character is missing or runs out, the function returns False. Otherwise, it returns True.

        Time Complexity:
            O(n + m): Where n is the length of ransomNote and m is the length of magazine. 
            The function iterates over the magazine to build the frequency counter and then 
            iterates over the ransomNote to check if the construction is possible.

        Space Complexity:
            O(1): The space used by the counter dictionary is proportional to the number of 
            unique characters in the magazine. Since there are only 26 possible lowercase English letters, 
            this is considered O(1) space.

        Args:
            ransomNote (str): The string representing the ransom note that needs to be constructed.
            magazine (str): The string representing the letters available in the magazine.

        Returns:
            bool: True if ransomNote can be constructed from magazine, otherwise False.
        """
        counter: Dict[str, int] = {}
        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        for c in ransomNote:
            if c in counter:
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]
            else:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("abc", "aabbcc", True),
        ("aab", "aa", False),
        ("", "anything", True),  # Edge case: Empty ransomNote
        ("anything", "", False),  # Edge case: Empty magazine
    ]

    for i, (ransomNote, magazine, expected) in enumerate(test_cases):
        result: bool = solution.canConstruct(ransomNote, magazine)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases passed!")