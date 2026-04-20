"""
2078. Two Furthest Houses With Different Colors

Problem Statement:
There are n houses evenly lined up on the street. You are given a 0-indexed
integer array colors of length n, where colors[i] represents the color of the
i-th house. Return the maximum distance between two houses with different colors.

Constraints:
- n == colors.length
- 2 <= n <= 100
- 0 <= colors[i] <= 100
- At least two houses have different colors.

Examples:

Example 1:
    Input: colors = [1,1,1,6,1,1,1]
    Output: 3

Example 2:
    Input: colors = [1,8,3,8,3]
    Output: 4

Example 3:
    Input: colors = [0,1]
    Output: 1
"""


class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        """
        Returns the maximum distance between two houses with different colors
        using two greedy scans from the ends.

        The furthest valid pair must include either the first house (index 0) or
        the last house (index N-1) as one endpoint — any pair not touching an
        endpoint can always be extended outward to a longer distance.

        Scan 1: from the right towards index 0 to find the furthest house with
                a different color from colors[0].
        Scan 2: from the left towards index N-1 to find the furthest house with
                a different color from colors[N-1].

        The answer is the maximum of the two distances found.

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        N: int = len(colors)

        d1: int = 0
        for i in range(N - 1, -1, -1):
            if colors[0] != colors[i]:
                d1 = i
                break

        d2: int = 0
        for j in range(N):
            if colors[-1] != colors[j]:
                d2 = (N - 1) - j
                break

        return max(d1, d2)

    def maxDistanceNaive(self, colors: list[int]) -> int:
        """
        Returns the maximum distance between two houses with different colors
        using a brute-force nested loop over all pairs.

        Time complexity:  O(n²)
        Space complexity: O(1)
        """
        N: int = len(colors)
        dist: int = 0

        for i in range(N):
            for j in range(i + 1, N):
                if colors[i] != colors[j]:
                    dist = max(dist, j - i)

        return dist


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 1, 1, 6, 1, 1, 1], 3),
        ([1, 8, 3, 8, 3],        4),
        ([0, 1],                  1),
        ([1, 1, 1, 1, 2],         4),
        ([1, 2, 1, 1, 1],         3),
    ]

    for label, method in [
        ("maxDistance     ", solution.maxDistance),
        ("maxDistanceNaive", solution.maxDistanceNaive),
    ]:
        for colors, expected in test_cases:
            result = method(colors)
            assert result == expected, \
                f"{label} failed on {colors}: expected {expected}, got {result}"
        print(f"  {label} passed")

    print("All test cases passed!")
