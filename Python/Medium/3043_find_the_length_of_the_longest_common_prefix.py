"""
3043. Find the Length of the Longest Common Prefix

Given two arrays of positive integers arr1 and arr2, find the length of the
longest common prefix (over decimal digit strings) between any pair (x, y)
with x in arr1 and y in arr2. Return 0 if no pair shares any prefix.

Problem Link: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

Examples:
    Example 1:
        Input: arr1 = [1, 10, 100], arr2 = [1000]
        Output: 3
        Explanation: 100 and 1000 share prefix "100".

    Example 2:
        Input: arr1 = [1, 2, 3], arr2 = [4, 4, 4]
        Output: 0

Constraints:
    1 <= arr1.length, arr2.length <= 5 * 10^4
    1 <= arr1[i], arr2[i] <= 10^8
"""


class TrieNode:
    def __init__(self):
        self.children: list["TrieNode | None"] = [None] * 10


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int) -> None:
        node = self.root
        for ch in str(num):
            idx = int(ch)
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]

    def find_longest_prefix(self, num: int) -> int:
        node = self.root
        length = 0
        for ch in str(num):
            idx = int(ch)
            if node.children[idx] is None:
                break
            length += 1
            node = node.children[idx]
        return length


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        """
        Prefix-set approach. Generate every prefix of every value in arr1 by
        repeatedly integer-dividing by 10 (each `n // 10` chops one digit).
        Then for each value in arr2, peel digits off until a prefix lands in
        the set — `len(str(n))` of the surviving number is the match length.

        Swapping so arr1 is the smaller side keeps the set as small as
        possible. Compared to the Trie variant, this avoids the per-node
        overhead and is faster in CPython.

        Time complexity:  O((n + m) * D), D = max digit count (= 9 here).
        Space complexity: O(n * D)
        """
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefix_set: set[int] = set()

        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n = n // 10

        res: int = 0
        for n in arr2:
            while n and n not in prefix_set:
                n = n // 10

            if n:
                res = max(res, len(str(n)))

        return res

    def longestCommonPrefixTrie(self, arr1: list[int], arr2: list[int]) -> int:
        """
        Classic 10-ary trie over digit strings: insert every value in arr1,
        then walk each value in arr2 down the trie counting matched digits.

        Algorithmically the same asymptotic cost as the prefix-set variant
        but with much heavier per-node overhead in Python.

        Time complexity:  O((n + m) * D)
        Space complexity: O(n * D)
        """
        trie = Trie()

        for num in arr1:
            trie.insert(num)

        longest_prefix = 0
        for num in arr2:
            longest_prefix = max(longest_prefix, trie.find_longest_prefix(num))

        return longest_prefix


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 10, 100], [1000], 3),
        ([1, 2, 3], [4, 4, 4], 0),
        ([1], [1], 1),
        ([12345], [12399], 3),
        ([100, 200], [3000, 4000], 0),
        ([987], [123, 9870, 9876], 3),
    ]

    for i, (arr1, arr2, expected) in enumerate(test_cases, 1):
        assert solution.longestCommonPrefix(list(arr1), list(arr2)) == expected, f"prefix-set test {i} failed"
        assert solution.longestCommonPrefixTrie(list(arr1), list(arr2)) == expected, f"trie test {i} failed"

    print("All test cases passed!")
