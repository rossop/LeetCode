"""
NOTE: it import to understand that given a list with n numbers and k valid numbers
    the values from k to n can be any numbers including val.
"""
from typing import List

class Solution:
    """
    A class to solve the 'Remove Element' problem.

    Problem:
        Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place.
        The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

        Example 1:
            Input: nums = [3,2,2,3], val = 3
            Output: 2, nums = [2,2,_,_]

        Example 2:
            Input: nums = [0,1,2,2,3,0,4,2], val = 2
            Output: 5, nums = [0,1,4,0,3,_,_,_]

    Constraints:
        - 0 <= nums.length <= 100
        - 0 <= nums[i] <= 50
        - 0 <= val <= 100
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of `val` from the list in-place and returns the number of remaining elements.

        Args:
            nums (List[int]): A list of integers.
            val (int): The value to remove from the list.

        Returns:
            int: The number of elements remaining in the list after removal.

        Time Complexity:
            O(n), where n is the length of the input list.

        Space Complexity:
            O(1), since the removal of elements is done in-place.
        """
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n


if __name__ == "__main__":
    # Test cases with expected outcomes
    test_cases = [
        ([3, 2, 2, 3], 3, (2, [2, 2])),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, (5, [0, 1, 4, 0, 3])),
        ([2, 2, 2], 2, (0, [])),
        ([1, 1, 1, 1, 1], 1, (0, [])),
        ([1], 1, (0, [])),
        ([1], 2, (1, [1]))
    ]

    # Initialize the Solution class
    solution = Solution()

    # Run the test cases
    for i, (nums, val, expected) in enumerate(test_cases, 1):
        k = solution.removeElement(nums, val)
        assert k == expected[0], f"Test case {i} failed: expected k = {expected[0]}, got {k}"
        assert sorted(nums[:k]) == sorted(expected[1]), f"Test case {i} failed: expected nums = {expected[1]}, got {nums[:k]}"
        print(f"Test case {i} passed: k = {k}, nums = {nums[:k]}")

    print("All test cases passed!")