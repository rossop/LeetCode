"""
2515. Shortest Distance to Target String in a Circular Array

Problem Statement:
You are given a 0-indexed circular string array words and a string target.
A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous
element of words[i] is words[(i - 1 + n) % n], where n is the length of words.

Starting from startIndex, you can move to either the next word or the previous
word with 1 step at a time.

Return the shortest distance needed to reach the string target. If the string
target does not exist in words, return -1.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] and target consist of only lowercase English letters
- 0 <= startIndex < words.length

Examples:

Example 1:
    Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
    Output: 1
    Explanation: Moving 1 unit to the left reaches index 0 ("hello").

Example 2:
    Input: words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
    Output: 1
    Explanation: Moving 1 unit to the left reaches index 2 ("leetcode").

Example 3:
    Input: words = ["i","eat","leetcode"], target = "ate", startIndex = 0
    Output: -1
    Explanation: "ate" does not exist in words.
"""

from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        """
        Returns the shortest distance from startIndex to any occurrence of target
        in the circular array, or -1 if target is not present.

        Iterates over every word by absolute index. For each occurrence of target,
        computes the direct distance diff = |i - startIndex|, then takes the shorter
        of the two circular paths: min(diff, n - diff). Uses n + 1 as a sentinel to
        detect the target-absent case without a separate membership check.

        Args:
            words (List[str]): The circular array of strings.
            target (str): The string to search for.
            startIndex (int): The index to start from.

        Returns:
            int: The minimum number of steps to reach target, or -1 if absent.

        Time Complexity:
            O(n): Single pass through the array.

        Space Complexity:
            O(1): No extra space used.
        """
        n: int = len(words)
        # Sentinel options:
        #   n + 1    — safe but loose; valid distances are in [0, n-1]
        #   n // 2 + 1 — tightest safe value; going both ways, the worst-case
        #                shortest distance is n // 2 (opposite side of the array),
        #                so n // 2 + 1 can never be a real result
        res: int = n // 2 + 1
        for i, word in enumerate(words):
            if word == target:
                diff = abs(i - startIndex)
                res = min(res, diff, n - diff)
        return res if res != n // 2 + 1 else -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["hello", "i", "am", "leetcode", "hello"], "hello", 1, 1),
        (["a", "b", "leetcode"], "leetcode", 0, 1),
        (["i", "eat", "leetcode"], "ate", 0, -1),
    ]

    for i, (words, target, startIndex, expected) in enumerate(test_cases, 1):
        result = solution.closetTarget(words, target, startIndex)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed")

    print("All test cases passed!")
