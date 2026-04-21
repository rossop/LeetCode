"""
1722. Minimize Hamming Distance After Swap Operations

Problem Statement:
You are given two integer arrays source and target, both of length n, and an
array allowedSwaps where allowedSwaps[i] = [ai, bi] means you can swap the
elements at indices ai and bi of source any number of times.

Return the minimum Hamming distance of source and target after performing any
amount of swap operations on source.

Constraints:
- n == source.length == target.length
- 1 <= n <= 10^5
- 1 <= source[i], target[i] <= 10^5
- 0 <= allowedSwaps.length <= 10^5
- allowedSwaps[i].length == 2
- 0 <= ai, bi <= n - 1
- ai != bi

Examples:

Example 1:
    Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
    Output: 1

Example 2:
    Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
    Output: 2

Example 3:
    Input: source = [5,1,2,4,3], target = [1,5,4,2,3],
           allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
    Output: 0
"""

from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.fa: list[int] = list(range(n))
        self.rank: list[int] = [0] * n

    def find(self, x: int) -> int:
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])  # path compression
        return self.fa[x]

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.fa[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class Solution:
    def minimumHammingDistance(
        self,
        source: List[int],
        target: List[int],
        allowedSwaps: List[List[int]],
    ) -> int:
        """
        Returns the minimum Hamming distance using Union-Find to group indices.

        Key insight: indices connected through allowedSwaps form a component
        within which source elements can be freely rearranged (swaps can be
        chained and repeated). The problem reduces to: for each component,
        how many target values cannot be matched by available source values?

        Algorithm:
        1. Build Union-Find: union every (a, b) pair from allowedSwaps.
        2. Group source values by component root into a frequency map.
        3. For each index i, check if target[i] is available in its component's
           frequency map. If yes, consume it (decrement). If no, add 1 to
           Hamming distance.

        Time complexity:  O(n + m·α(n)) where m = len(allowedSwaps) and
                          α is the inverse Ackermann function (near-constant).
        Space complexity: O(n)
        """
        n: int = len(source)
        uf = UnionFind(n)

        for a, b in allowedSwaps:
            uf.union(a, b)

        sets: dict = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            f = uf.find(i)
            sets[f][source[i]] += 1

        ans: int = 0
        for i in range(n):
            f = uf.find(i)
            if sets[f][target[i]] > 0:
                sets[f][target[i]] -= 1
            else:
                ans += 1

        return ans

    def minimumHammingDistanceDFS(
        self,
        source: List[int],
        target: List[int],
        allowedSwaps: List[List[int]],
    ) -> int:
        """
        Returns the minimum Hamming distance using DFS to find connected components.

        Builds an adjacency list from allowedSwaps, then finds all connected
        components via DFS. Within each component, counts source and target value
        frequencies and greedily matches them: for each source value, the number
        of matches is min(source_freq[v], target_freq[v]). Unmatched positions
        contribute to Hamming distance.

        Time complexity:  O(n + m) where m = len(allowedSwaps).
        Space complexity: O(n + m) for the adjacency list and visited set.
        """
        n = len(source)
        G: list[list[int]] = [[] for _ in range(n)]
        for a, b in allowedSwaps:
            G[a].append(b)
            G[b].append(a)

        visited: set[int] = set()
        ans = 0

        def dfs(node: int, connected: set[int]) -> None:
            if node in connected:
                return
            connected.add(node)
            for child in G[node]:
                dfs(child, connected)

        for i in range(n):
            if i in visited:
                continue
            connected: set[int] = set()
            dfs(i, connected)

            counter_src: dict[int, int] = defaultdict(int)
            counter_tgt: dict[int, int] = defaultdict(int)
            for j in connected:
                counter_src[source[j]] += 1
                counter_tgt[target[j]] += 1

            unmatched = len(connected)
            for k, v in counter_src.items():
                unmatched -= min(v, counter_tgt[k])
            ans += unmatched
            visited |= connected

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]], 1),
        ([1, 2, 3, 4], [1, 3, 2, 4], [],               2),
        ([5, 1, 2, 4, 3], [1, 5, 4, 2, 3], [[0, 4], [4, 2], [1, 3], [1, 4]], 0),
        ([1], [1], [], 0),
        ([1], [2], [], 1),
    ]

    for label, method in [
        ("minimumHammingDistance   ", solution.minimumHammingDistance),
        ("minimumHammingDistanceDFS", solution.minimumHammingDistanceDFS),
    ]:
        for source, target, swaps, expected in test_cases:
            result = method(source, target, swaps)
            assert result == expected, \
                f"{label} failed: source={source}, target={target}, swaps={swaps} → expected {expected}, got {result}"
        print(f"  {label} passed")

    print("All test cases passed!")
