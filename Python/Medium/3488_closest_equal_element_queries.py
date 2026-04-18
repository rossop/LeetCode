"""
3488. Closest Equal Element Queries

Problem Statement:
You are given a circular array nums and an array queries.

For each query i, you have to find the minimum distance between the element at
index queries[i] and any other index j in the circular array, where
nums[j] == nums[queries[i]]. If no such index exists, the answer for that
query should be -1.

Return an array answer of the same size as queries, where answer[i] represents
the result for query i.

Constraints:
- 1 <= queries.length <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
- 0 <= queries[i] < nums.length

Examples:

Example 1:
    Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]
    Output: [2,-1,3]
    Explanation:
        Query 0: nums[0] = 1. Nearest same value is at index 2, distance 2.
        Query 1: nums[3] = 4. No other index contains 4, result is -1.
        Query 2: nums[5] = 3. Nearest same value is at index 1, distance 3.

Example 2:
    Input: nums = [1,2,3,4], queries = [0,1,2,3]
    Output: [-1,-1,-1,-1]
    Explanation: All values are unique, so every query returns -1.
"""

import bisect


class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        positions: dict[int, list[int]] = {}
        for i, num in enumerate(nums):
            if num in positions:
                positions[num].append(i)
            else:
                positions[num] = [i]

        def find_minimum_distance(positions: dict[int, list[int]], q: int) -> int:
            indices = positions[nums[q]]
            if len(indices) == 1:
                return -1
            n: int = len(nums)
            m: int = len(indices)
            p: int = bisect.bisect_left(indices, q)
            res: int = n
            for neighbour in (indices[(p - 1) % m], indices[(p + 1) % m]):
                diff = abs(neighbour - q)
                res = min(res, diff, n - diff)
            return res

        answers: list[int] = [-1] * len(queries)
        for i, q in enumerate(queries):
            answers[i] = find_minimum_distance(positions, q)

        return answers

    def solveQueriesNaive(self, nums: list[int], queries: list[int]) -> list[int]:
        def find_minimum_distance(nums: list[int], q: int) -> int:
            n: int = len(nums)
            for i in range(1, n):
                right: int = (q + i) % n
                left: int = (q - i) % n
                if nums[left] == nums[q] or nums[right] == nums[q]:
                    return i
            return -1

        answers: list[int] = [-1] * len(queries)
        for i, q in enumerate(queries):
            answers[i] = find_minimum_distance(nums, q)

        return answers


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 3, 1, 4, 1, 3, 2], [0, 3, 5], [2, -1, 3]),
        ([1, 2, 3, 4], [0, 1, 2, 3], [-1, -1, -1, -1]),
        ([3, 3], [1], [1]),
    ]

    for i, (nums, queries, expected) in enumerate(test_cases, 1):
        result = solution.solveQueries(nums, queries)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed")

    print("All test cases passed!")
