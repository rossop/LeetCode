"""
NOTES
When looking at other people times my solution does not seem to beat other ones by much. 
This code is only in the 28% percentile. Even adding a solution using map doesn't speed up much the solution. 
"""

from typing import List

class Solution:
    """
    A class to solve the 'Longest Common Prefix' problem.

    Problem:
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".

        Example 1:
            Input: strs = ["flower", "flow", "flight"]
            Output: "fl"

        Example 2:
            Input: strs = ["dog", "racecar", "car"]
            Output: ""
            Explanation: There is no common prefix among the input strings.

    Constraints:
        - 1 <= strs.length <= 200
        - 0 <= strs[i].length <= 200
        - strs[i] consists of only lowercase English letters.
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix string among an array of strings.

        This method first determines the length of the shortest string in the array. 
        It then iterates over each character index (up to the length of the shortest string) 
        and checks whether all strings in the array have the same character at that index.
        If they do, the character is added to the result. If not, the loop breaks and the current
        prefix is returned.

        Args:
            strs (List[str]): A list of strings to find the longest common prefix.

        Returns:
            str: The longest common prefix shared among all strings in the list. 
                 If there is no common prefix, an empty string is returned.

        Time Complexity:
            O(S * n), where S is the length of the shortest string in the list, 
            and n is the number of strings. In the worst case, we compare each character of the 
            shortest string with all other strings.

        Space Complexity:
            O(S), where S is the length of the shortest string. This is the space required 
            to store the output list that will eventually be joined into a string.
        """
        if not strs:
            return ""

        # Find the length of the shortest string in the list
        S = min(map(len, strs))
        
        # Initialize an empty list to store the common prefix characters
        output = []
        
        # Iterate over each character position up to the length of the shortest string
        for i in range(S):
            # Take the character from the first string as the reference
            c = strs[0][i]
            
            # Compare this character with the corresponding character in all other strings
            if all(s[i] == c for s in strs):
                output.append(c)
            else:
                # If we found a mismatch, break out of the loop
                break
        
        # Join the list of characters into a string and return
        return "".join(output)
    
    def longestCommonPrefixMap(self, strs: List[str]) -> str:
        """
        An alternative implementation using the map function and all.

        This method also finds the longest common prefix by using map to check if
        all characters at each index are the same across all strings.

        Args:
            strs (List[str]): A list of strings to find the longest common prefix.

        Returns:
            str: The longest common prefix shared among all strings in the list. 
                 If there is no common prefix, an empty string is returned.

        Time Complexity:
            O(S * n), where S is the length of the shortest string in the list, 
            and n is the number of strings. In the worst case, we compare each character of the 
            shortest string with all other strings.

        Space Complexity:
            O(S), where S is the length of the shortest string. This is the space required 
            to store the output list that will eventually be joined into a string.
        """
        if not strs:
            return ""

        # Find the length of the shortest string in the list
        S = min(map(len, strs))
        
        # Initialize an empty list to store the common prefix characters
        output = []
        
        # Iterate over each character position up to the length of the shortest string
        for i in range(S):
            # Take the character from the first string as the reference
            c = strs[0][i]
            
            # Use map to check if all characters at position i are equal to c
            if all(map(lambda x: x[i] == c, strs)):
                output.append(c)
            else:
                break
                
        return "".join(output)

    def longestCommonPrefixManual(self, strs: List[str]) -> str:
        """
        An alternative implementation that manually checks for common characters
        without using the all or map functions.

        This method iterates over each character index (up to the length of the shortest string)
        and uses a loop to check if all strings have the same character at that index.
        If they do, the character is added to the result. If not, the loop breaks.

        Args:
            strs (List[str]): A list of strings to find the longest common prefix.

        Returns:
            str: The longest common prefix shared among all strings in the list. 
                 If there is no common prefix, an empty string is returned.

        Time Complexity:
            O(S * n), where S is the length of the shortest string in the list, 
            and n is the number of strings. In the worst case, we compare each character of the 
            shortest string with all other strings.

        Space Complexity:
            O(S), where S is the length of the shortest string. This is the space required 
            to store the output list that will eventually be joined into a string.
        """
        if not strs:
            return ""
        
        # Find the length of the shortest string in the list
        S = min(map(len, strs))
        
        # Initialize an empty list to store the common prefix characters
        output = []
        
        # Iterate over each character position up to the length of the shortest string
        for i in range(S):
            # Assume all characters at the current position are equal
            char_equal = True
            
            # Take the character from the first string as the reference
            c = strs[0][i]
            
            # Compare this character with the corresponding character in all other strings
            for s in strs:
                if s[i] != c:
                    char_equal = False
                    break
            
            # If all characters at the current position are equal, add the character to the output
            if char_equal:
                output.append(c)
            else:
                # If we found a mismatch, break out of the loop
                break
        
        # Join the list of characters into a string and return
        return "".join(output)




if __name__ == "__main__":
    # Test cases with expected outcomes
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["throne", "throne"], "throne"),
        (["throne", "dungeon"], ""),
        ([""], ""),
        (["a"], "a"),
        (["a", "a", "a"], "a")
    ]

    # Test cases with expected outcomes
    solution = Solution()
    
    # Run the test cases for all three methods
    for i, (strs, expected) in enumerate(test_cases, 1):
        assert solution.longestCommonPrefix(strs) == expected, f"Method 1, Test case {i} failed"
        assert solution.longestCommonPrefixMap(strs) == expected, f"Method 2, Test case {i} failed"
        assert solution.longestCommonPrefixManual(strs) == expected, f"Method 3, Test case {i} failed"

    print("All test cases passed!")