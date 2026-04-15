"""
1646. Get Maximum in Generated Array

Problem Statement:
You are given an integer n. A 0-indexed integer array nums of length n + 1 is
generated in the following way:

    nums[0] = 0
    nums[1] = 1
    nums[2 * i] = nums[i]               when 2 <= 2 * i <= n
    nums[2 * i + 1] = nums[i] + nums[i + 1]  when 2 <= 2 * i + 1 <= n

Return the maximum integer in the array nums.

Constraints:
- 0 <= n <= 100

Examples:

Example 1:
    Input: n = 7
    Output: 3
    Explanation: nums = [0,1,1,2,1,3,2,3], and the maximum is 3.

Example 2:
    Input: n = 2
    Output: 1
    Explanation: nums = [0,1,1]. The maximum is 1.

Example 3:
    Input: n = 3
    Output: 2
    Explanation: nums = [0,1,1,2]. The maximum is 2.
"""


class Solution:
    def getMaximumGeneratedNaive(self, n: int) -> int:
        """
        Computes the maximum of the generated array using naive recursion.

        Recursively computes each index by applying the even/odd rules, with no
        caching. Overlapping subproblems are recomputed on every call, leading to
        exponential work for large n.

        Args:
            n (int): The upper bound index; the generated array has length n + 1.

        Returns:
            int: The maximum value in the generated array.

        Time Complexity:
            O(2^n): Each call branches into two recursive calls with no caching.

        Space Complexity:
            O(n): Call stack depth proportional to n.
        """
        def generate(i: int) -> int:
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i % 2 == 0:
                return generate(i // 2)
            return generate(i // 2) + generate(i // 2 + 1)

        return max(generate(i) for i in range(n + 1))

    def getMaximumGeneratedMemo(self, n: int) -> int:
        """
        Computes the maximum of the generated array using memoized recursion (top-down DP).

        Same recursive structure as naive recursion, but stores each computed value
        in a cache on the way down. Cache hits short-circuit further recursion,
        reducing redundant work to zero.

        Args:
            n (int): The upper bound index; the generated array has length n + 1.

        Returns:
            int: The maximum value in the generated array.

        Time Complexity:
            O(n): Each index is computed exactly once.

        Space Complexity:
            O(n): Cache and call stack, each of depth n.
        """
        memo: dict[int, int] = {}

        def generate(i: int) -> int:
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i in memo:
                return memo[i]
            if i % 2 == 0:
                memo[i] = generate(i // 2)
            else:
                memo[i] = generate(i // 2) + generate(i // 2 + 1)
            return memo[i]

        return max(generate(i) for i in range(n + 1))

    def getMaximumGenerated(self, n: int) -> int:
        """
        Builds the generated array iteratively (tabulation) and returns its maximum.

        Allocates an array of length n + 1, sets the base cases, then fills each
        index using the even/odd rules. Returns the maximum value in the array.

        Args:
            n (int): The upper bound index; the generated array has length n + 1.

        Returns:
            int: The maximum value in the generated array.

        Time Complexity:
            O(n): Single pass to fill the array.

        Space Complexity:
            O(n): The array of length n + 1.
        """
        nums: list[int] = [0] * ( n+1 )
        for ii in range(n+1):
            if ii == 0:
                nums[0] = 0
                continue
            if ii == 1:
                nums[1] = 1
                continue
            if ii%2 ==0:
                nums[ii] = nums[ii//2]
            else:
                nums[ii] = nums[ii//2] + nums[ii//2 +1]
        return max(nums)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (7, 3),
        (2, 1),
        (3, 2),
    ]

    for label, method in [
        ("Naive", solution.getMaximumGeneratedNaive),
        ("Memo", solution.getMaximumGeneratedMemo),
        ("Tabulation", solution.getMaximumGenerated),
    ]:
        print(f"--- {label} ---")
        for i, (n, expected) in enumerate(test_cases, 1):
            result = method(n)
            assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
            print(f"  Test case {i} passed")

    print("All test cases passed!")
