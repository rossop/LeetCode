import heapq
from typing import List

"""
1405. Longest Happy String

Problem Statement:
A string s is called happy if it satisfies the following conditions:
- s only contains the letters 'a', 'b', and 'c'.
- s does not contain any of "aaa", "bbb", or "ccc" as a substring.
- s contains at most a occurrences of the letter 'a'.
- s contains at most b occurrences of the letter 'b'.
- s contains at most c occurrences of the letter 'c'.

Given three integers a, b, and c, return the longest possible happy string.
If there are multiple longest happy strings, return any of them.
If there is no such string, return the empty string "".

Examples:
Example 1:
    Input: a = 1, b = 1, c = 7
    Output: "ccaccbcc"
    Explanation: "ccbccacc" would also be a correct answer.

Example 2:
    Input: a = 7, b = 1, c = 0
    Output: "aabaa"
    Explanation: It is the only correct answer in this case.

Constraints:
- 0 <= a, b, c <= 100
- a + b + c > 0
"""

class Solution:
    """
    This class provides a method to generate the longest happy string based on
    the counts of 'a', 'b', and 'c'. A "happy" string is one that does not
    contain three consecutive identical letters.
    """

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Generates the longest possible happy string using the counts of 'a', 'b',
        and 'c'. The algorithm uses a max-heap to always append the character
        with the most remaining occurrences while ensuring that no character is
        appended three times consecutively.

        Time Complexity: O((a + b + c) log 3) = O(a + b + c), where a, b, and c
        are the counts of characters.

        Space Complexity: O(1) (not counting the result string space).

        Args:
            a (int): Number of 'a' characters allowed.
            b (int): Number of 'b' characters allowed.
            c (int): Number of 'c' characters allowed.

        Returns:
            str: The longest happy string possible.
        """
        res: str = ""
        maxHeap: List[Tuple[int, str]] = []

        # Push negative counts and characters to the heap to simulate max-heap
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count: int
            char: str
            count, char = heapq.heappop(maxHeap)

            # If the last two characters are the same as the current one,
            # use the second most frequent one
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break  # No other characters to use, so we can't proceed
                count2: int
                char2: str
                count2, char2 = heapq.heappop(maxHeap)  # Get 2nd most frequent
                res += char2  # Append it to the result string
                count2 += 1  # Decrease its count
                if count2:  # If occurrences left, push it back to the heap
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                # Append the most frequent character and adjust its count
                res += char
                count += 1  # Increase the count (since it's negative)

            # Push the character back to the heap if there are still occurrences
            if count:
                heapq.heappush(maxHeap, (count, char))

        return res


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: a = 1, b = 1, c = 7
    result: str = solution.longestDiverseString(1, 1, 7)
    assert result == "ccaccbcc" or result == "ccbccacc", (
        f"Test Case 1 Failed! Got {result}"
    )

    # Test Case 2: a = 7, b = 1, c = 0
    result = solution.longestDiverseString(7, 1, 0)
    assert result == "aabaa", f"Test Case 2 Failed! Got {result}"

    # Test Case 3: a = 2, b = 2, c = 1
    result = solution.longestDiverseString(2, 2, 1)
    assert result in {"aabbc", "bbaac", "ababc", "babac", "abbac"}, (
        f"Test Case 3 Failed! Got {result}"
    )

    # Test Case 4: a = 0, b = 0, c = 0
    result = solution.longestDiverseString(0, 0, 0)
    assert result == "", f"Test Case 4 Failed! Got {result}"

    # Test Case 5: a = 3, b = 3, c = 3
    result = solution.longestDiverseString(3, 3, 3)
    assert result in {"abcabcabc", "bcabcabca"}, (
        f"Test Case 5 Failed! Got {result}"
    )

    print("All test cases passed!")
