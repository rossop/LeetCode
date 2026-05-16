"""
1431. Kids With the Greatest Number of Candies

Given candies[i] for n kids and extraCandies to give away, return a boolean
array where result[i] is true if kid i — after receiving all extraCandies —
ties or beats the original maximum.

Problem Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Examples:
    Example 1:
        Input: candies = [2, 3, 5, 1, 3], extraCandies = 3
        Output: [true, true, true, false, true]

    Example 2:
        Input: candies = [4, 2, 1, 1, 2], extraCandies = 1
        Output: [true, false, false, false, false]

    Example 3:
        Input: candies = [12, 1, 12], extraCandies = 10
        Output: [true, false, true]

Constraints:
    n == candies.length
    2 <= n <= 100
    1 <= candies[i] <= 100
    1 <= extraCandies <= 50
"""


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """
        Compute the current max once, then check candy + extraCandies >= max
        for each kid. The threshold doesn't change as candy is only added.

        Time complexity:  O(n)
        Space complexity: O(n) — for the output array.
        """
        target: int = max(candies)
        ans: list[bool] = [False] * len(candies)
        for i, candy in enumerate(candies):
            ans[i] = (candy + extraCandies) >= target

        return ans

    def kidsWithCandiesMap(self, candies: list[int], extraCandies: int) -> list[bool]:
        """
        Functional variant: map the threshold check over candies. Same
        algorithm, just expressed via map + lambda.

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        target: int = max(candies)
        return list(
            map(
                lambda x: (x + extraCandies) >= target,
                candies,
            )
        )


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
        ([1, 1], 1, [True, True]),
    ]

    for i, (candies, extra, expected) in enumerate(test_cases, 1):
        assert solution.kidsWithCandies(list(candies), extra) == expected, f"kidsWithCandies test {i} failed"
        assert solution.kidsWithCandiesMap(list(candies), extra) == expected, f"kidsWithCandiesMap test {i} failed"

    print("All test cases passed!")
