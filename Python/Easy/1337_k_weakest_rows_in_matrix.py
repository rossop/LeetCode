"""
1337. The K Weakest Rows in a Matrix
Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:
1. The number of soldiers in row i is less than the number of soldiers in row j.
2. Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

TOPICS: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix
"""

import heapq
from typing import List

class Solution:
    """
    Solution class for the "The K Weakest Rows in a Matrix" problem.

    This class provides three methods to solve the problem:
    1. `kWeakestRows`: A simple approach using sorting.
    2. `kWeakestRowsOptimized`: An optimized approach using binary search.
    3. `kWeakestRowsHeap`: An approach using a heap to maintain the k weakest rows.
    """

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Simple approach to find the k weakest rows in the matrix by sorting.

        Time Complexity: O(m * n + m * log m)
        Space Complexity: O(m)

        Args:
            mat (List[List[int]]): The binary matrix representing soldiers and civilians.
            k (int): The number of weakest rows to return.

        Returns:
            List[int]: The indices of the k weakest rows, ordered from weakest to strongest.
        """
        m: int = len(mat)

        # Calculate the strength of each row
        strength = [(sum(row), i) for i, row in enumerate(mat)]
        
        # Sort by strength and then by index
        strength.sort()
        
        # Extract the indices of the k weakest rows
        weakness_order = [j for _, j in strength]
        return weakness_order[:k]

    def kWeakestRowsOptimized(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Optimized version using binary search to find the number of soldiers in each row.

        Time Complexity: O(m * log n + m * log m)
        Space Complexity: O(m)

        Args:
            mat (List[List[int]]): The binary matrix representing soldiers and civilians.
            k (int): The number of weakest rows to return.

        Returns:
            List[int]: The indices of the k weakest rows, ordered from weakest to strongest.
        """
        def binary_search(row: List[int]) -> int:
            """
            Finds the number of soldiers (1's) in a row using binary search.
            """
            low, high = 0, len(row)
            while low < high:
                mid = (low + high) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low

        m: int = len(mat)

        # Calculate the strength of each row using binary search
        strength = [(binary_search(row), i) for i, row in enumerate(mat)]
        
        # Sort by strength and then by index
        strength.sort()
        
        # Extract the indices of the k weakest rows
        weakness_order = [j for _, j in strength]
        return weakness_order[:k]

    def kWeakestRowsHeap(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Finds the k weakest rows in the matrix using a heap.

        Time Complexity: O(m * log k)
        Space Complexity: O(k)

        Args:
            mat (List[List[int]]): The binary matrix representing soldiers and civilians.
            k (int): The number of weakest rows to return.

        Returns:
            List[int]: The indices of the k weakest rows, ordered from weakest to strongest.
        """
        heap = []
        for i, row in enumerate(mat):
            strength = sum(row)  # Calculate the strength (number of soldiers)
            heapq.heappush(heap, (strength, i))
        
        # Extract the indices of the k weakest rows
        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3, [2,0,3]),  # Example 1
        ([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], 2, [0,2]),  # Example 2
        ([[1,0],[1,0],[1,0],[0,0],[1,1]], 3, [3,0,1]),  # Edge case: Some rows with equal soldiers
        ([[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,0]], 2, [0,1]),  # Edge case: Rows with only civilians
    ]

    methods = [
        solution.kWeakestRows,
        solution.kWeakestRowsOptimized,
        solution.kWeakestRowsHeap
    ]

    for method in methods:
        for i, (mat, k, expected) in enumerate(test_cases, 1):
            result = method(mat, k)
            assert result == expected, f"Test case {i} failed for {method.__name__}: expected {expected}, got {result}"

    print("All test cases passed!")