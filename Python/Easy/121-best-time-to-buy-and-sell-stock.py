from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given
        stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one
        stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction.
        If you cannot achieve any profit, return 0.

        Args:
            prices (List[int]): List of stock prices.

        Returns:
            int: The maximum profit achievable from a single buy and sell
                transaction.

        Examples:
            Example 1:
                Input: prices = [7,1,5,3,6,4]
                Output: 5
                Explanation: Buy on day 2 (price = 1) and
                    sell on day 5 (price = 6), profit = 6-1 = 5.

            Example 2:
                Input: prices = [7,6,4,3,1]
                Output: 0
                Explanation: In this case, no transactions are done and
                    the max profit = 0.
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# Example usage:
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(solution.maxProfit([7, 6, 4, 3, 1]))    # Output: 0
print(solution.maxProfit([2, 4, 1]))          # Output: 2
