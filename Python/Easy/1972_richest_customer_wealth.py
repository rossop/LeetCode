"""
This class provides a solution to the problem of finding the richest customer
wealth.

Given a 2D list where each row represents a customer and each element in the
row represents the amount of money that customer has in a particular bank, the
goal is to return the maximum wealth among all customers.

Method:
    maximumWealth: Calculates the maximum wealth of any customer by summing
    their bank balances and finding the maximum sum.

Example:
    Input: accounts = [[1,2,3],[3,2,1]]
    Output: 6
"""

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Calculate the maximum wealth among all customers.

        Args:
            accounts (List[List[int]]): 2D list representing each customer's
            bank accounts.

        Returns:
            int: The maximum wealth of any customer.
        """
        return max(map(sum, accounts))


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([[1, 2, 3], [3, 2, 1]], 6),
        ([[1, 5], [7, 3], [3, 5]], 10),
        ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
        ([[10, 5, 2], [3, 1, 4], [9, 9, 1]], 17),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 15),
    ]

    for i, (accs, expected) in enumerate(test_cases):
        result = solution.maximumWealth(accs)
        assert result == expected, f"""
        Test case {i+1} failed: expected {expected}, got {result}"""

    print("All test cases passed!")
