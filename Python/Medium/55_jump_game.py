"""
55. Jump Game

You start at index 0 of nums; each nums[i] is the maximum jump length from
that position. Return whether the last index is reachable.

Problem Link: https://leetcode.com/problems/jump-game/

Examples:
    Example 1:
        Input: nums = [2, 3, 1, 1, 4]
        Output: true

    Example 2:
        Input: nums = [3, 2, 1, 0, 4]
        Output: false

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^5
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Greedy, right-to-left. Track the leftmost index `target` from which
        the goal is known reachable. Walk backwards: any i where
        i + nums[i] >= target can replace target, dragging the frontier left.
        Goal is reachable iff target collapses to 0.

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        n: int = len(nums)
        target: int = n - 1

        for i in range(n - 1, -1, -1):
            max_jump: int = nums[i]
            if i + max_jump >= target:
                target = i

        return target == 0

    def canJumpMemoisation(self, nums: list[int]) -> bool:
        """
        Top-down DP. can_reach(i) is true if any jump 1..nums[i] lands on a
        cell from which the end is reachable; cache results to keep each i
        from being recomputed.

        Time complexity:  O(n^2) — worst case (max jump = n - i).
        Space complexity: O(n)
        """
        n: int = len(nums)
        memo: dict[int, bool] = {n - 1: True}

        def can_reach(i: int) -> bool:
            if i in memo:
                return memo[i]

            for jump in range(1, nums[i] + 1):
                if can_reach(i + jump):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return can_reach(0)

    def canJumpRecursive(self, nums: list[int]) -> bool:
        """
        Plain recursion with no memo — exponential. Kept as a baseline to
        show what memoisation actually saves.

        Time complexity:  O(max(nums)^n) — exponential branching.
        Space complexity: O(n) — recursion depth.
        """
        n: int = len(nums)

        def can_reach(i: int) -> bool:
            if i == n - 1:
                return True

            for jump in range(1, nums[i] + 1):
                if can_reach(i + jump):
                    return True

            return False

        return can_reach(0)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([2, 0, 0], True),
        ([1, 0, 1, 0], False),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.canJump(list(nums)) == expected, f"canJump test {i} failed"
        assert solution.canJumpMemoisation(list(nums)) == expected, f"canJumpMemoisation test {i} failed"
        assert solution.canJumpRecursive(list(nums)) == expected, f"canJumpRecursive test {i} failed"

    print("All test cases passed!")
