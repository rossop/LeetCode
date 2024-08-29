from typing import List, Dict
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together from a list of strings. Anagrams are words that contain
        the exact same characters in any order.

        Optimized Approach:
        Time Complexity: O(N * K * log(K)) where N is the length of strs and K is the maximum 
        length of a string in strs. Sorting each string takes O(K * log(K)) and we do this for 
        every string in strs.
        Space Complexity: O(N * K) for storing the grouped anagrams.

        Args:
            strs (List[str]): The list of strings to group by anagrams.

        Returns:
            List[List[str]]: A list of lists, where each sublist contains anagrams.
        """
        anagrams: Dict[str, List[str]] = defaultdict(list)

        for s in strs:
            # Sort the string and use it as a key
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        
        return list(anagrams.values())

    def groupAnagramsInitial(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together using a brute-force method with a visited list to keep track 
        of grouped strings. Less efficient but functional.

        Initial Approach:
        Time Complexity: O(N^2 * K) where N is the length of strs and K is the maximum 
        length of a string in strs. For each string, we compare it with every other string.
        Space Complexity: O(N * K) for storing the grouped anagrams.

        Args:
            strs (List[str]): The list of strings to group by anagrams.

        Returns:
            List[List[str]]: A list of lists, where each sublist contains anagrams.
        """
        n: int = len(strs)
        group: List[str] = []
        G: List[List[str]] = []
        visited: List[int] = []

        p1: int = 0

        while p1 < n:
            if p1 not in visited:
                s: str = strs[p1]
                group.append(s)
                chars = sorted([c for c in s])
                visited.append(p1)
                
                for i in range(p1 + 1, n):
                    new_s: str = strs[i]
                    if i not in visited and sorted([c for c in new_s]) == chars:
                        group.append(new_s)
                        visited.append(i)
                
                G.append(group)
                group = []  # Reset the group for the next set of anagrams
            
            p1 += 1

        return G


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]
    
    solution = Solution()

    # Test the optimized approach
    for i, (strs, expected) in enumerate(test_cases):
        result = solution.groupAnagrams(strs)
        assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected]), \
            f"Optimized Approach - Test case {i + 1} failed: expected {expected}, got {result}"

    # Test the initial approach
    for i, (strs, expected) in enumerate(test_cases):
        result = solution.groupAnagramsInitial(strs)
        assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected]), \
            f"Initial Approach - Test case {i + 1} failed: expected {expected}, got {result}"
    
    print("All test cases passed!")