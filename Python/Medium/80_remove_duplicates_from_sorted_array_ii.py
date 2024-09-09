from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from the sorted array `nums` in-place such that each unique element
        appears at most twice. The function modifies the input list and returns the length `k`
        of the modified list where the first `k` elements are the required result.

        Time Complexity:
            O(n): The list is traversed once, where `n` is the length of the input list.

        Space Complexity:
            O(1): The function uses a constant amount of extra space.

        Args:
            nums (List[int]): A sorted list of integers where duplicates may exist.

        Returns:
            int: The length `k` of the modified list with at most two occurrences of each element.
        """
        if not nums:
            return 0

        n: int = len(nums)
        c: int = 1  # Counter to track occurrences of the current element
        j: int = 1  # Pointer to place the next valid element

        for i in range(1, n):
            # Manage the counter
            if nums[i] == nums[i - 1]:
                c += 1
            else:
                c = 1

            # Place the element if its occurrence is within the allowed limit
            if c <= 2:
                nums[j] = nums[i]
                j += 1

        return j

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
        ([1, 1], 2, [1, 1]),
        ([1, 1, 1, 1], 2, [1, 1]),
        ([1], 1, [1]),
        ([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3], 7, [0, 0, 1, 1, 2, 2, 3]),
    ]

    for i, (nums, expected_length, expected_nums) in enumerate(test_cases):
        nums_copy = nums.copy()  # Copy to preserve the original list for comparison
        length = solution.removeDuplicates(nums_copy)
        assert length == expected_length, f"Test case {i+1} failed: expected length {expected_length}, got {length}"
        assert nums_copy[:length] == expected_nums, f"Test case {i+1} failed: expected nums {expected_nums}, got {nums_copy[:length]}"
    
    print("All test cases passed!")