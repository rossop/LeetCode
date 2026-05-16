"""
875. Koko Eating Bananas

Koko picks an integer eating speed k. Each hour she eats up to k bananas from
one pile. Return the minimum k that finishes every pile within h hours.

Problem Link: https://leetcode.com/problems/koko-eating-bananas/

Examples:
    Example 1:
        Input: piles = [3, 6, 7, 11], h = 8
        Output: 4

    Example 2:
        Input: piles = [30, 11, 23, 4, 20], h = 5
        Output: 30

    Example 3:
        Input: piles = [30, 11, 23, 4, 20], h = 6
        Output: 23

Constraints:
    1 <= piles.length <= 10^4
    piles.length <= h <= 10^9
    1 <= piles[i] <= 10^9
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Binary search on k over [1, max(piles)]. For each candidate k the
        hours needed are sum(ceil(p / k)); the predicate "hours <= h" is
        monotonic in k, so the standard lower-bound search finds the minimum.

        Time complexity:  O(n log m), n = len(piles), m = max(piles).
        Space complexity: O(1)
        """
        def calc_rate(piles: list[int], k: int) -> int:
            return sum((x + k - 1) // k for x in piles)

        left, right = 1, max(piles)
        res = right

        while left <= right:
            k: int = left + (right - left) // 2
            if calc_rate(piles, k) <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res

    def minEatingSpeedBruteForce(self, piles: list[int], h: int) -> int:
        """
        Linear scan over every candidate k from 1 to max(piles). Useful as a
        baseline / cross-check; far too slow for the real constraints.

        Time complexity:  O(n * m)
        Space complexity: O(1)
        """
        def calc_rate(piles: list[int], k: int) -> int:
            return sum((x + k - 1) // k for x in piles)

        k_min, k_max = 1, max(piles)
        for k in range(k_min, k_max + 1):
            if calc_rate(piles, k) <= h:
                return k

        return -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
        ([1], 1, 1),
        ([1000000000], 2, 500000000),
    ]

    for i, (piles, h, expected) in enumerate(test_cases, 1):
        result = solution.minEatingSpeed(list(piles), h)
        assert result == expected, f"minEatingSpeed test {i} failed: expected {expected}, got {result}"

    # Brute force only on small inputs.
    for piles, h, expected in test_cases[:4]:
        assert solution.minEatingSpeedBruteForce(list(piles), h) == expected

    print("All test cases passed!")
