"""
624. Maximum Distance in Arrays
https://leetcode.com/problems/maximum-distance-in-arrays
"""
from typing import List

class Solution:
    def maxDistanceOptimized(self, arrays: List[List[int]]) -> int:
        """
        Optimized approach to find the maximum distance between any two elements
        from different arrays.

        This method iterates through the arrays while keeping track of the minimum 
        and maximum values seen so far, updating the maximum distance on the go.

        Time Complexity:
            O(m): Where m is the number of arrays.
        
        Space Complexity:
            O(1): Constant space usage.

        Args:
            arrays (List[List[int]]): A list of sorted arrays.

        Returns:
            int: The maximum distance.
        """
        ans: int = 0
        mini: int = float('inf')  # Initialize to a high value based on problem constraints
        maxi: int = -float('inf')  # Initialize to a low value based on problem constraints
        
        for arr in arrays:
            # Update the maximum distance with the current array's extremes
            ans = max(ans, arr[-1] - mini, maxi - arr[0])
            # Update the minimum and maximum seen so far
            mini = min(mini, arr[0])
            maxi = max(maxi, arr[-1])
        
        return ans

    def maxDistanceEfficient(self, arrays: List[List[int]]) -> int:
        """
        Efficiently calculates the maximum distance by keeping track of the 
        first and last elements of the arrays, ensuring that the selected 
        minimum and maximum values come from different arrays.

        Time Complexity:
            O(m): Where m is the number of arrays.

        Space Complexity:
            O(1): Constant space usage.

        Args:
            arrays (List[List[int]]): A list of sorted arrays.

        Returns:
            int: The maximum distance between any two integers from different arrays.
        """
        min1: int = float('inf')
        min2: int = float('inf')
        max1: int = float('-inf')
        max2: int = float('-inf')
        min1_idx: int = -1
        max1_idx: int = -1
        
        for i, array in enumerate(arrays):
            first: int = array[0]
            last: int = array[-1]
            
            if first < min1:
                min2, min1 = min1, first
                min1_idx = i
            elif first < min2:
                min2 = first
            
            if last > max1:
                max2, max1 = max1, last
                max1_idx = i
            elif last > max2:
                max2 = last
        
        if min1_idx != max1_idx:
            return max1 - min1
        else:
            return max(max1 - min2, max2 - min1)

    def maxDistanceNaive(self, arrays: List[List[int]]) -> int:
        """
        Naive approach to calculate the maximum distance between the minimum 
        and maximum elements from different arrays.

        This method calculates the min and max for the arrays, then checks if 
        they belong to different arrays. If not, it checks the second min and max.

        Time Complexity:
            O(m * n): Where m is the number of arrays and n is the length of the longest array.

        Space Complexity:
            O(m): For storing start and end elements of arrays.

        Args:
            arrays (List[List[int]]): A list of sorted arrays.

        Returns:
            int: The maximum distance between any two integers from different arrays.
        """
        start: List[int] = []
        end: List[int] = []

        for a in arrays:
            start.append(a[0])
            end.append(a[-1])
        
        max_end: int = max(end)
        min_start: int = min(start)

        if end.index(max_end) == start.index(min_start):
            end.remove(max_end)
            second_max_val: int = max(end)
            start.remove(min_start)
            second_min_val: int = min(start)
            return max(max_end - second_min_val, second_max_val - min_start)
        return max_end - min_start


if __name__ == '__main__':
    solution = Solution()

    # Test cases
    test_cases = [
        ([[1,2,3], [4,5], [1,2,3]], 4),
        ([[1], [1]], 0),
        ([[1,5], [3,4], [2,3]], 3),
        ([[10,12,14], [1,3,7], [5,6,8]], 13),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 8),
    ]

    for i, (arrays, expected) in enumerate(test_cases):
        result_optimized: int = solution.maxDistanceOptimized(arrays)
        result_efficient: int = solution.maxDistanceEfficient(arrays)
        result_naive: int = solution.maxDistanceNaive(arrays)
        
        assert result_optimized == expected, f"Test case {i+1} failed for optimized solution: expected {expected}, got {result_optimized}"
        assert result_efficient == expected, f"Test case {i+1} failed for efficient solution: expected {expected}, got {result_efficient}"
        assert result_naive == expected, f"Test case {i+1} failed for naive solution: expected {expected}, got {result_naive}"

    print("All test cases passed!")
