"""
1331. Rank Transform of an Array

Problem Statement:
Given an array of integers arr, replace each element with its rank. The rank represents how large the element is.
- Rank starts from 1.
- The larger the element, the larger the rank.
- If two elements are equal, their rank must be the same.

Example 1:
    Input: arr = [40, 10, 20, 30]
    Output: [4, 1, 2, 3]

Example 2:
    Input: arr = [100, 100, 100]
    Output: [1, 1, 1]

Example 3:
    Input: arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]

Constraints:
- 0 <= arr.length <= 10^5
- -10^9 <= arr[i] <= 10^9
"""

from typing import List, Tuple, Dict

class Solution:
    """
    This class provides three different methods to transform an array into its rank array.
    
    Methods:
    1. arrayRankTransformOptimised: Optimized method using sorting and ranks.
    2. arrayRankTransform: Method based on dictionary to map ranks to values.
    3. arrayRankTransformSorting: Simplified sorting-based approach.
    """

    def arrayRankTransformOptimised(self, arr: List[int]) -> List[int]:
        """
        Optimized approach using sorting and tracking ranks based on previous values.

        Time Complexity: O(n log n), due to sorting the array.
        Space Complexity: O(n), to store the sorted array and result.

        Args:
            arr: List[int] - The input array.

        Returns:
            List[int] - The rank-transformed array.
        """
        if not arr:
            return []

        # Step 1: Sort the array along with original indices
        sorted_arr: List[Tuple[int, int]] = sorted((num, i) for i, num in enumerate(arr))

        # Step 2: Initialize rank array and rank tracker
        rank = 1
        result: List[int] = [0] * len(arr)
        prev_num: int = sorted_arr[0][0]

        # Step 3: Assign ranks based on sorted order
        result[sorted_arr[0][1]] = rank
        for i in range(1, len(sorted_arr)):
            num, index = sorted_arr[i]
            if num != prev_num:
                rank += 1  # Increment rank if the number changes
            result[index] = rank
            prev_num = num

        return result

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Uses a dictionary to assign ranks after sorting unique values.

        Time Complexity: O(n log n), due to sorting the unique elements.
        Space Complexity: O(n), for storing the rank map and result array.

        Args:
            arr: List[int] - The input array.

        Returns:
            List[int] - The rank-transformed array.
        """
        hashmap: Dict[int, int] = {}
        rank_counter: int = 1

        # Sort the unique values and assign ranks
        for n in sorted(set(arr)):
            hashmap[n] = rank_counter
            rank_counter += 1

        # Replace each element in the array with its rank
        return [hashmap[n] for n in arr]

    def arrayRankTransformSorting(self, arr: List[int]) -> List[int]:
        """
        Simplified approach: sort, remove duplicates, map numbers to ranks.

        Time Complexity: O(n log n), due to sorting.
        Space Complexity: O(n), for storing the rank map and result.

        Args:
            arr: List[int] - The input array.

        Returns:
            List[int] - The rank-transformed array.
        """
        if not arr:
            return []

        # Step 1: Sort and remove duplicates
        sorted_unique: List[int] = sorted(set(arr))

        # Step 2: Create a dictionary that maps each number to its rank
        rank_map: Dict[int, int] = {num: i + 1 for i, num in enumerate(sorted_unique)}

        # Step 3: Replace each element in the original array with its rank
        return [rank_map[n] for n in arr]


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ([40, 10, 20, 30], [4, 1, 2, 3]),
        ([100, 100, 100], [1, 1, 1]),
        ([37, 12, 28, 9, 100, 56, 80, 5, 12], [5, 3, 4, 2, 8, 6, 7, 1, 3]),
    ]

    solution = Solution()

    # Test the optimised method
    print("Testing arrayRankTransformOptimised method:")
    for i, (arr, expected) in enumerate(test_cases):
        result = solution.arrayRankTransformOptimised(arr)
        assert result == expected, f"Test case {i+1} failed (Optimised): Expected {expected}, but got {result}"
    print("All test cases passed for arrayRankTransformOptimised method!")

    # Test the dictionary-based method
    print("\nTesting arrayRankTransform method:")
    for i, (arr, expected) in enumerate(test_cases):
        result = solution.arrayRankTransform(arr)
        assert result == expected, f"Test case {i+1} failed (Dictionary): Expected {expected}, but got {result}"
    print("All test cases passed for arrayRankTransform method!")

    # Test the sorting-based method
    print("\nTesting arrayRankTransformSorting method:")
    for i, (arr, expected) in enumerate(test_cases):
        result = solution.arrayRankTransformSorting(arr)
        assert result == expected, f"Test case {i+1} failed (Sorting): Expected {expected}, but got {result}"
    print("All test cases passed for arrayRankTransformSorting method!")
