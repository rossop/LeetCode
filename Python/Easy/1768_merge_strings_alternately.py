class Solution:
    """
    1768. Merge Strings Alternately
    
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
    starting with word1. If a string is longer than the other, append the additional letters onto the 
    end of the merged string.
    
    Return the merged string.
    
    Example 1:
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    
    Example 2:
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    
    Example 3:
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    
    Constraints:
    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
    """

    def mergeAlternately_map(self, word1: str, word2: str) -> str:
        """
        Merges two strings alternately using map and lambda.

        Time Complexity: O(n1 + n2), where n1 is the length of word1, and n2 is the length of word2.
        Space Complexity: O(n1 + n2), for storing the final merged string.
        """
        max_len = max(len(word1), len(word2))
        
        merged = ''.join(map(lambda i: (word1[i] if i < len(word1) else '') + 
                                         (word2[i] if i < len(word2) else ''), range(max_len)))
        
        return merged

    def mergeAlternately_while(self, word1: str, word2: str) -> str:
        """
        Merges two strings alternately using a while loop.

        Time Complexity: O(n1 + n2), where n1 is the length of word1, and n2 is the length of word2.
        Space Complexity:O(n1 + n2), for storing the final merged string.
        """
        merged = []
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)

        while i < n1 or j < n2:
            if i < n1:
                merged.append(word1[i])
                i += 1
            if j < n2:
                merged.append(word2[j])
                j += 1
        
        return ''.join(merged)
    

    def mergeAlternately(self, word1: str, word2: str) -> str:
        """ 
        Merges two stings alternatively using while loops
        
        Time Complexity: O(n)
        Time Complexity: O(A + B) where A is Length of word1, B is Length of word2
        Space Complexity: O(A + B) where- A is Length of word1, B is Length of word2
        """
        A, B = len(word1), len(word2)
        a, b = 0, 0
        s = []

        word = 1
        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            else:
                s.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            s.append(word1[a])
            a += 1
        
        while b < B:
            s.append(word2[b])
            b += 1
        
        return ''.join(s)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd")
    ]
    
    solution = Solution()
    
    for word1, word2, expected in test_cases:
        result_map = solution.mergeAlternately_map(word1, word2)
        result_while = solution.mergeAlternately_while(word1, word2)
        
        assert result_map == expected, f"Map method failed on {word1}, {word2}. Expected: {expected}, Got: {result_map}"
        assert result_while == expected, f"While method failed on {word1}, {word2}. Expected: {expected}, Got: {result_while}"
    
    print("All test cases passed!")
