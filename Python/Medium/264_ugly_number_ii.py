"""
264. Ugly Number II
Link: https://leetcode.com/problems/ugly-number-ii/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Constraints:
1 <= n <= 1690
"""

import heapq
from typing import List

class Solution:
    """
    Solution class for finding the nth Ugly Number using different approaches.
    """

    def nth_ugly_number(self, n: int) -> int:
        """
        Returns the nth ugly number using the dynamic programming approach.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Initialise DP array with 1s as first ugly number
        ugly_numbers: List[int] = [1] * n # dp

        # Initialise pointers for multiple of 2, 3, and 5
        index_2: int
        index_3: int
        index_5: int 
        index_2, index_3, index_5 = 0, 0, 0

        # Generate ugly numbers up to the nth one
        for i in range(1, n):
            # Calculate the next multiples for 2, 3, and 5
            next_2: int = ugly_numbers[index_2] * 2
            next_3: int = ugly_numbers[index_3] * 3
            next_5: int = ugly_numbers[index_5] * 5

            # Select the minimum of these multiples to be the next ugly number
            ugly_numbers[i] = min(next_2, next_3, next_5)

            # Increment the corresponding indice when their multiples are used
            # This avoids repetition of one number
            if ugly_numbers[i] == next_2:
                index_2 += 1
            if ugly_numbers[i] == next_3:
                index_3 += 1
            if ugly_numbers[i] == next_5:
                index_5 += 1

        # Return the nth ugly number
        return ugly_numbers[n - 1]

    def nth_ugly_number_heap(self, n: int) -> int:
        """
        Returns the nth ugly number using the min-heap approach.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        min_heap = [1]
        heapq.heapify(min_heap)
        seen = {1}
        factors = [2, 3, 5]
        ugly_number = 1

        for _ in range(n):
            ugly_number = heapq.heappop(min_heap)

            for factor in factors:
                new_ugly = ugly_number * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(min_heap, new_ugly)

        return ugly_number


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (10, 12),  # Example 1
        (1, 1),    # Example 2
        (15, 24),  # Check for 15th ugly number
        (100, 1536),  # Check for 100th ugly number
        (1690, 2123366400),  # Check for the maximum value of n
    ]
    
    methods = [
        solution.nth_ugly_number,
        solution.nth_ugly_number_heap,
    ]
    
    for method in methods:
        for i, (n, expected) in enumerate(test_cases, 1):
            result = method(n)
            assert result == expected, f"Test case {i} failed for {method.__name__}: expected {expected}, got {result}"
    
    print("All test cases passed!")