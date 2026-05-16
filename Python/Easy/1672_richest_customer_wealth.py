"""
1672. Richest Customer Wealth

Given an m x n grid accounts where accounts[i][j] is customer i's balance at
bank j, return the maximum total wealth across all customers.

Problem Link: https://leetcode.com/problems/richest-customer-wealth/

Examples:
    Example 1:
        Input: accounts = [[1, 2, 3], [3, 2, 1]]
        Output: 6

    Example 2:
        Input: accounts = [[1, 5], [7, 3], [3, 5]]
        Output: 10

    Example 3:
        Input: accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        Output: 17

Constraints:
    m == accounts.length
    n == accounts[i].length
    1 <= m, n <= 50
    1 <= accounts[i][j] <= 100
"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        """
        Sum each customer's row and track the running max. Single pass over
        the grid — no need to materialize the per-customer totals.

        Time complexity:  O(m * n)
        Space complexity: O(1)
        """
        ans: int = 0
        for acc in accounts:
            ans = max(sum(acc), ans)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 2, 3], [3, 2, 1]], 6),
        ([[1, 5], [7, 3], [3, 5]], 10),
        ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
        ([[100]], 100),
    ]

    for i, (accounts, expected) in enumerate(test_cases, 1):
        result = solution.maximumWealth(accounts)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")
