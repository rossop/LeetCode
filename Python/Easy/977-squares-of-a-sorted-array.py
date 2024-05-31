from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums sorted in non-decreasing order, return an array of the
        squares of each number sorted in non-decreasing order.

        This implementation uses a two-pointer technique to achieve O(n) time complexity.

        Args:
            nums (List[int]): An integer array sorted in non-decreasing order.

        Returns:
            List[int]: An array of the squares of each number sorted in non-decreasing order.

        Time Complexity:
            O(n): We traverse the array once using the two-pointer technique.

        Examples:
            Example 1:
                Input: nums = [-4, -1, 0, 3, 10]
                Output: [0, 1, 9, 16, 100]
                Explanation: After squaring, the array becomes [16, 1, 0, 9, 100].
                             After sorting, it becomes [0, 1, 9, 16, 100].

            Example 2:
                Input: nums = [-7, -3, 2, 3, 11]
                Output: [4, 9, 9, 49, 121]
        """
        n = len(nums)
        res = [0] * n
        L, R = 0, n-1
        for i in range(n-1, -1, -1):
            if abs(nums[L]) > abs(nums[R]):
                val = nums[L] ** 2
                L += 1
            else:
                val = nums[R] ** 2
                R -= 1
            res[i] = val
        return res

    def sortedSquaresNlogN(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums sorted in non-decreasing order, return an array of the
        squares of each number sorted in non-decreasing order.

        This implementation first squares each element and then sorts the array,
        resulting in O(n log n) time complexity.

        Args:
            nums (List[int]): An integer array sorted in non-decreasing order.

        Returns:
            List[int]: An array of the squares of each number sorted in non-decreasing order.

        Time Complexity:
            O(n log n): Squaring each element takes O(n) and sorting takes O(n log n).

        Examples:
            Example 1:
                Input: nums = [-4, -1, 0, 3, 10]
                Output: [0, 1, 9, 16, 100]
                Explanation: After squaring, the array becomes [16, 1, 0, 9, 100].
                             After sorting, it becomes [0, 1, 9, 16, 100].

            Example 2:
                Input: nums = [-7, -3, 2, 3, 11]
                Output: [4, 9, 9, 49, 121]
        """
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        return sorted(nums)

    def sortedSquaresOptimized(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums sorted in non-decreasing order, return an array of the
        squares of each number sorted in non-decreasing order.

        This implementation uses a two-pointer technique to achieve O(n) time complexity.

        Args:
            nums (List[int]): An integer array sorted in non-decreasing order.

        Returns:
            List[int]: An array of the squares of each number sorted in non-decreasing order.

        Time Complexity:
            O(n): We traverse the array once using the two-pointer technique.

        Examples:
            Example 1:
                Input: nums = [-4, -1, 0, 3, 10]
                Output: [0, 1, 9, 16, 100]
                Explanation: After squaring, the array becomes [16, 1, 0, 9, 100].
                             After sorting, it becomes [0, 1, 9, 16, 100].

            Example 2:
                Input: nums = [-7, -3, 2, 3, 11]
                Output: [4, 9, 9, 49, 121]
        """
        n = len(nums)
        res = [0] * n
        L, R = 0, n-1
        for i in range(n-1, -1, -1):
            if abs(nums[L]) > abs(nums[R]):
                res[i] = nums[L] ** 2
                L += 1
            else:
                res[i] = nums[R] ** 2
                R -= 1
        return res

# Example usage:
solution = Solution()
print(solution.sortedSquares([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]
print(solution.sortedSquaresNlogN([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]
print(solution.sortedSquaresOptimized([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]

