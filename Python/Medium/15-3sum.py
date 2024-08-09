from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        This function sorts the array and then uses the two-pointer technique to find 
        all unique triplets that sum up to zero. The sorted array allows for efficient 
        identification of triplets, and duplicates are avoided by checking the current 
        number against the previous one.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            List[List[int]]: A list of lists, where each inner list contains three integers 
                             that sum up to zero.

        Time Complexity:
            O(n^2): The array is sorted first (O(n log n)) and then each element is processed 
            with a two-pointer scan (O(n) for each of the n elements).

        Space Complexity:
            O(n): The solution uses O(n) space to store the output list. No extra space is 
            needed beyond this.

        Example:
            Input: nums = [-1, 0, 1, 2, -1, -4]
            Output: [[-1, -1, 2], [-1, 0, 1]]
            Explanation: The distinct triplets are [-1, -1, 2] and [-1, 0, 1].

        Constraints:
            3 <= nums.length <= 3000
            -10^5 <= nums[i] <= 10^5
        """
        nums.sort()
        n: int = len(nums)
        sol: List[List[int]] = []

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L: int = i + 1
            R: int = n - 1
            while L < R:
                summ = nums[i] + nums[L] + nums[R]
                if summ < 0:
                    L += 1
                elif summ > 0:
                    R -= 1
                else:
                    sol.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1

        return sol


if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]])
    ]

    # Validate the test cases
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.threeSum(nums)
        assert sorted(result) == sorted(expected), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases passed!")