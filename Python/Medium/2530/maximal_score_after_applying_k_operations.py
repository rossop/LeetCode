"""
2530. Maximal Score After Applying K Operations

Problem Statement:
You are given a 0-indexed integer array nums and an integer k. You have a
starting score of 0.

In one operation:
- Choose an index i such that 0 <= i < nums.length.
- Increase your score by nums[i], and replace nums[i] with ceil(nums[i] / 3).

Return the maximum possible score you can attain after applying exactly k
operations.

The ceiling function ceil(val) is the least integer greater than or equal
to val.

Example 1:
    Input: nums = [10, 10, 10, 10, 10], k = 5
    Output: 50
    Explanation: Apply the operation to each array element exactly once.
                 The final score is 10 + 10 + 10 + 10 + 10 = 50.

Example 2:
    Input: nums = [1, 10, 3, 3, 3], k = 3
    Output: 17
    Explanation:
        Operation 1: Select i = 1, so nums becomes [1, 4, 3, 3, 3].
            Your score increases by 10.
        Operation 2: Select i = 1, so nums becomes [1, 2, 3, 3, 3].
            Your score increases by 4.
        Operation 3: Select i = 2, so nums becomes [1, 1, 1, 3, 3].
            Your score increases by 3.
        The final score is 10 + 4 + 3 = 17.

Constraints:
- 1 <= nums.length, k <= 10^5
- 1 <= nums[i] <= 10^9
"""

import heapq
from math import ceil
from typing import List


class Solution:
    """
    This class provides two methods to solve the problem of maximizing the
    score after applying K operations. In each operation, the largest element
    is added to the score and then reduced by replacing it with
    ceil(element / 3).

    Methods:
    1. maxKelements: An optimized solution using a max-heap to retrieve the
    largest element in O(log n) time.
    2. maxKelementsBruteForce: A brute-force solution that searches for the
    largest element in the list and replaces it.
    """

    def maxKelements(self, nums: List[int], k: int) -> int:
        """
        Solves the problem using a max-heap to efficiently find and update the
        largest element in each operation.

        Time Complexity: O(k log n), where k is the number of operations and n
        is the number of elements in nums. Space Complexity: O(n), where n is
        the number of elements in nums to store the heap.

        Args:
            nums: A list of integers representing the array. k: An integer
            representing the number of operations.

        Returns:
            int: The maximum possible score after k operations.
        """
        count: int = 0
        max_heap: List[int] = []

        # Convert nums into a max-heap (using negative values since heapq is a
        # min-heap by default)
        for num in nums:
            heapq.heappush(max_heap, -num)

        # Perform k operations
        while k > 0:
            k -= 1
            # Extract the largest element (remember to negate)
            max_value: int = -heapq.heappop(max_heap)
            count += max_value  # Add it to the score

            # Push the reduced value (ceil(max_value / 3)) back into the heap
            heapq.heappush(max_heap, -ceil(max_value / 3))

        return count

    def maxKelementsBruteForce(self, nums: List[int], k: int) -> int:
        """
        Solves the problem using a brute-force approach by finding the largest
        element in the list for each operation.

        Time Complexity: O(k * n), where k is the number of operations and n is
        the number of elements in nums. Space Complexity: O(1), aside from the
        input list nums.

        Args:
            nums: A list of integers representing the array. k: An integer
            representing the number of operations.

        Returns:
            int: The maximum possible score after k operations.
        """
        count: int = 0

        # Perform k operations
        while k > 0:
            k -= 1
            max_value: int = max(nums)  # Find the largest element
            count += max_value  # Add it to the score

            # Replace the max element with ceil(max_value / 3)
            max_pos: int = nums.index(max_value)
            nums[max_pos] = ceil(nums[max_pos] / 3)

        return count
