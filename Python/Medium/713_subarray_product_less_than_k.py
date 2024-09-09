from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Counts the number of contiguous subarrays where the product of all the elements 
        is strictly less than k using a sliding window approach.

        The sliding window (two-pointer) approach efficiently finds the number of subarrays 
        by maintaining a window with a product less than k and expanding or contracting the 
        window as needed.

        Time Complexity:
            O(n): The algorithm iterates over the list of numbers with the right pointer 
            and adjusts the left pointer as needed.

        Space Complexity:
            O(1): No extra space proportional to the input size is used, only a few integer 
            variables are utilized.

        Args:
            nums (List[int]): The input list of positive integers.
            k (int): The threshold for the product of subarrays.
        
        Returns:
            int: The count of subarrays whose product is less than k.
        """
        if k <= 1:
            return 0

        count: int = 0
        prod: int = 1
        left: int = 0

        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            count += right - left + 1

        return count

    def numSubarrayProductLessThanK_Inefficient(self, nums: List[int], k: int) -> int:
        """
        Counts the number of contiguous subarrays where the product of all the elements 
        is strictly less than k using a brute-force approach.

        This method is inefficient because it considers every possible subarray, 
        calculating their product individually. The inefficiency arises because it repeatedly 
        calculates overlapping subarrays, leading to unnecessary recomputation.

        Time Complexity:
            O(n^2): The algorithm uses a nested loop where the outer loop starts a subarray, 
            and the inner loop extends it, leading to quadratic time complexity.

        Space Complexity:
            O(n^2): This version unnecessarily stores all subarrays, leading to high space usage.

        Args:
            nums (List[int]): The input list of positive integers.
            k (int): The threshold for the product of subarrays.
        
        Returns:
            int: The count of subarrays whose product is less than k.
        """
        n: int = len(nums)
        prod: List[List[int]] = []
        
        for p1 in range(n):
            val: int = 1
            p2: int = p1
            arr: List[int] = []
            while p2 < n:
                val *= nums[p2]
                if val < k:
                    arr.append(nums[p2])
                    prod.append(arr.copy())
                    p2 += 1
                else:
                    break
        
        return len(prod)

if __name__ == "__main__":
    solution = Solution()

    test_cases: List[tuple[List[int], int, int]] = [
        ([10, 5, 2, 6], 100, 8),  # Expected output is 8
        ([1, 2, 3], 0, 0),        # Expected output is 0
        ([1, 2, 3], 7, 6),        # Expected output is 4
        ([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19, 18),  # Expected output is 18
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result: int = solution.numSubarrayProductLessThanK(nums, k)
        assert result == expected, f"Test case {i+1} failed for the efficient solution: expected {expected}, got {result}"
        
        result_inefficient: int = solution.numSubarrayProductLessThanK_Inefficient(nums, k)
        assert result_inefficient == expected, f"Test case {i+1} failed for the inefficient solution: expected {expected}, got {result_inefficient}"

    print("All test cases passed!")