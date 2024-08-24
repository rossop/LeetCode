from typing import List


class Solution:
    """
    3190. Find Minimum Operations to Make All Elements Divisible by Three

    This class provides methods to find the minimum number of operations
    required to make all elements in a given list divisible by 3. Each
    operation can either add or subtract 1 from any element of the list.

    Problem Link:
    https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
    """

    def minimumOperations(self, nums: List[int]) -> int:
        """
        Returns the minimum number of operations to make all elements divisible
        by 3.

        Time Complexity: O(n), where n is the length of the nums list.
        Space Complexity: O(1), no additional space other than input
        and minimal variables.

        Args:
        nums (List[int]): List of integers.

        Returns:
        int: Minimum number of operations.
        """
        return sum(min(num % 3, 3 - num % 3) for num in nums)

    def minimumOperationsAlternative(self, nums: List[int]) -> int:
        """
        Alternative method to achieve the same result using a different
        approach.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
        nums (List[int]): List of integers.

        Returns:
        int: Minimum number of operations.
        """
        operations: int = 0
        for num in nums:
            remainder: int = num % 3
            operations += min(remainder, 3 - remainder)
        return operations


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4], 3),      # Test case 1
        ([3, 6, 9], 0),         # Test case 2
        ([4, 8, 11, 13], 4),    # Additional test case
    ]

    # Run the test cases
    for i, (numbers, expected) in enumerate(test_cases, 1):
        result = solution.minimumOperations(numbers)
        assert result == expected, f"""
        Test case {i} failed: expected {expected}, got {result}
        """
        print(f"Test case {i} passed.")

        # Test alternative method
        result_alt = solution.minimumOperationsAlternative(numbers)
        assert result_alt == expected, f"""
        Alternative solution for test case {i} failed:
        expected {expected}, got {result_alt}
        """
        print(f"Alternative solution for test case {i} passed.")

    print("All test cases passed!")
