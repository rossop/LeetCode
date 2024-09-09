from typing import List


class Solution:
    """
    A class used to solve the 'Best Time to Buy and Sell Stock' problem.

    Problem:
        You are given an array 'prices' where 'prices[i]' is the price of a given stock on the i-th day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different
        day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If no profit can be made, return 0.

        Example 1:
            Input: prices = [7, 1, 5, 3, 6, 4]
            Output: 5
            Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

        Example 2:
            Input: prices = [7, 6, 4, 3, 1]
            Output: 0
            Explanation: In this case, no transactions are done, and the max profit = 0.

    Constraints:
        - 1 <= prices.length <= 10^5
        - 0 <= prices[i] <= 10^4
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        An alternative method to calculate the maximum profit from a single buy and sell transaction.

        This method uses a straightforward approach by iterating through the list of prices, 
        updating the minimum price seen so far, and calculating the potential profit at each step.

        Args:
            prices (list[int]): A list of integers representing the price of a stock on different days.

        Returns:
            int: The maximum profit achievable. If no profit can be made, returns 0.

        Time Complexity:
            O(n): The algorithm only requires a single pass through the 'prices' list, where 'n' is the length of the list.

        Space Complexity:
            O(1): The algorithm uses a constant amount of extra space (just a few variables).
        """
        S = len(prices)
        if S == 0:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in range(1, S):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit
    
    def maxProfitAlternative(self, prices: list[int]) -> int:
        """
        Calculates the maximum profit that can be achieved from a single buy and sell transaction.

        This method uses a single pass through the list of prices while keeping track of the minimum price 
        seen so far and the maximum profit that can be achieved if the stock is sold on the current day.

        Args:
            prices (list[int]): A list of integers representing the price of a stock on different days.

        Returns:
            int: The maximum profit achievable. If no profit can be made, returns 0.

        Time Complexity:
            O(n): The algorithm only requires a single pass through the 'prices' list, where 'n' is the length of the list.

        Space Complexity:
            O(1): The algorithm uses a constant amount of extra space (just a few variables).
        """

        min_price = float('inf')  # Initialize the min_price to a very high value
        max_profit = 0  # Initialize max_profit to 0
        
        for price in prices:
            # If the current price is lower than the min_price, update min_price
            if price < min_price:
                min_price = price
            
            # Calculate the potential profit if selling at the current price
            potential_profit = price - min_price
            
            # If the potential profit is greater than the max_profit, update max_profit
            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit


if __name__ == "__main__":
    # Test cases with expected outcomes
    solution = Solution()
    
    # Test cases for the first method
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5, "maxProfit, Test case 1 failed"
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0, "maxProfit, Test case 2 failed"
    assert solution.maxProfit([1, 2, 3, 4, 5, 6]) == 5, "maxProfit, Test case 3 failed"
    assert solution.maxProfit([7, 1, 5, 3, 6, 4, 8, 2]) == 7, "maxProfit, Test case 4 failed"
    assert solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 4, "maxProfit, Test case 5 failed"
    assert solution.maxProfit([2, 4, 1]) == 2, "maxProfit, Test case 6 failed"

    # Test cases for the alternative method
    assert solution.maxProfitAlternative([7, 1, 5, 3, 6, 4]) == 5, "maxProfitAlternative, Test case 1 failed"
    assert solution.maxProfitAlternative([7, 6, 4, 3, 1]) == 0, "maxProfitAlternative, Test case 2 failed"
    assert solution.maxProfitAlternative([1, 2, 3, 4, 5, 6]) == 5, "maxProfitAlternative, Test case 3 failed"
    assert solution.maxProfitAlternative([7, 1, 5, 3, 6, 4, 8, 2]) == 7, "maxProfitAlternative, Test case 4 failed"
    assert solution.maxProfitAlternative([3, 3, 5, 0, 0, 3, 1, 4]) == 4, "maxProfitAlternative, Test case 5 failed"
    assert solution.maxProfitAlternative([2, 4, 1]) == 2, "maxProfitAlternative, Test case 6 failed"
    
    print("All test cases passed!")