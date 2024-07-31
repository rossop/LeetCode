from typing import List

class Solution:
    """
    A class to solve the 'Remove Duplicates from Sorted Array' problem.

    Problem:
        Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place 
        such that each unique element appears only once. The relative order of the elements should be 
        kept the same. Then return the number of unique elements in `nums`.

        Example 1:
            Input: nums = [1,1,2]
            Output: 2, nums = [1,2,_]

        Example 2:
            Input: nums = [0,0,1,1,1,2,2,3,3,4]
            Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

    Constraints:
        - 1 <= nums.length <= 3 * 10^4
        - -100 <= nums[i] <= 100
        - nums is sorted in non-decreasing order.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted list in-place and returns the number of unique elements.

        Args:
            nums (List[int]): A sorted list of integers.

        Returns:
            int: The number of unique elements in `nums`.

        Time Complexity:
            O(n), where n is the length of the input list.

        Space Complexity:
            O(1), since the removal of duplicates is done in-place.
        """
        n = len(nums)
        if n == 0:
            return 0

        j = 1  # InitialisŸe the index for the next unique element

        # Iterate through the list starting from the second element
        for i in range(1, n):
            # If the current element is not equal to the previous element
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j


if __name__ == "__main__":
    # Test cases with expected outcomes
    test_cases = [
        ([1, 1, 2], (2, [1, 2])),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], (5, [0, 1, 2, 3, 4])),
        ([1, 2, 3, 4, 5], (5, [1, 2, 3, 4, 5])),
        ([1, 1, 1, 1, 1], (1, [1])),
        ([1], (1, [1]))
    ]

    # Initialise the Solution class
    solution = Solution()

    # Run the test cases
    for i, (nums, expected) in enumerate(test_cases, 1):
        k = solution.removeDuplicates(nums)
        assert k == expected[0], f"Test case {i} failed: expected k = {expected[0]}, got {k}"
        assert nums[:k] == expected[1], f"Test case {i} failed: expected nums = {expected[1]}, got {nums[:k]}"
        print(f"Test case {i} passed: k = {k}, nums = {nums[:k]}")

    print("All test cases passed!")