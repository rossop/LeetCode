from typing import List

class Solution:
    """
    A class to solve the 'Product of Array Except Self' problem.

    Problem:
        Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product 
        of all the elements of `nums` except `nums[i]`.

        The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.

        Example 1:
            Input: nums = [1,2,3,4]
            Output: [24,12,8,6]

        Example 2:
            Input: nums = [-1,1,0,-3,3]
            Output: [0,0,9,0,0]

    Constraints:
        - 2 <= nums.length <= 10^5
        - -30 <= nums[i] <= 30
        - The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

    Follow-up:
        Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Computes the product of all elements except the current one for each element in the array.

        This method uses a two-pass approach:
        1. The first pass calculates the prefix product (product of all elements to the left of the current element).
        2. The second pass calculates the suffix product (product of all elements to the right of the current element).
        The result for each element is the product of its prefix and suffix products.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: A list of products where each element is the product of all other elements except itself.

        Time Complexity:
            O(N), where N is the length of the input list. The function makes two passes through the list.

        Space Complexity:
            O(1) extra space (excluding the output list). The calculation is done in-place using the output list.
        """
        N: int = len(nums)
        products: List[int] = [1] * N
        
        # Prefix
        left_product = 1
        for n in range(N):
            products[n] *= left_product
            left_product *= nums[n]
        
        # Suffix
        right_product = 1
        for n in range(N-1, -1, -1):
            products[n] *= right_product
            right_product *= nums[n]

        return products

    def productExceptSelfBruteForce(self, nums: List[int]) -> List[int]:
        """
        A brute-force approach to compute the product of all elements except the current one.

        This method calculates the product of all other elements for each element in the array using nested loops.
        This is not an efficient solution, as it has a time complexity of O(N^2).

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: A list of products where each element is the product of all other elements except itself.

        Time Complexity:
            O(N^2), where N is the length of the input list. This is due to the nested loops.

        Space Complexity:
            O(N) for the output list.
        """
        N: int = len(nums)
        products: List[int] = []
        for n in range(N):
            product = 1
            for m in range(N):
                if n != m:
                    product *= nums[m]
            products.append(product)
        return products


if __name__ == "__main__":
    # Test cases with expected outcomes
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([1, 0], [0, 1]),
        ([10, 3, 5, 6, 2], [180, 600, 360, 300, 900])
    ]

    # Initialize the Solution class
    solution = Solution()

    # Run the test cases for both methods
    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.productExceptSelf(nums) == expected, f"Optimised method, Test case {i} failed"
        assert solution.productExceptSelfBruteForce(nums) == expected, f"Brute-force method, Test case {i} failed"

    print("All test cases passed!")