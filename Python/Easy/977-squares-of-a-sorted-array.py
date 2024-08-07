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
        n: int = len(nums)
        res: List[int] = []
        L: int = 0 
        R: int = n-1

        while L <= R:
            if abs(nums[R]) > abs(nums[L]):
                sq = nums[R]**2
                R -= 1
            else:
                sq = nums[L]**2
                L += 1
            res.append(sq)
        res.reverse()  # The optimised solution avoids the need for reversing 
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
        nums = [n**2 for n in nums]
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
        n: int = len(nums)
        res: List[int] = [0] * n
        L: int = 0 
        R: int = n-1
        for i in range(n-1, -1, -1):
            if abs(nums[L]) > abs(nums[R]):
                res[i] = nums[L] ** 2
                L += 1
            else:
                res[i] = nums[R] ** 2
                R -= 1
        return res


if __name__ == "__main__":
    solution = Solution()

    # Test cases with expected outcomes
    test_cases = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([-5, -3, -2, -1], [1, 4, 9, 25]),
        ([0, 1, 2, 3, 4], [0, 1, 4, 9, 16]),
        ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
        ([-1, 0, 1], [0, 1, 1]),
    ]
    for i, (input_list, expected) in enumerate(test_cases, 1):
        assert solution.sortedSquares(input_list.copy()) == expected, f"Test case {i} failed for sortedSquares"
        assert solution.sortedSquaresNlogN(input_list.copy()) == expected, f"Test case {i} failed for sortedSquaresNlogN"
        assert solution.sortedSquaresOptimized(input_list.copy()) == expected, f"Test case {i} failed for sortedSquaresOptimized"
        print(f"Test case {i} passed")

    print("All test cases passed!")

