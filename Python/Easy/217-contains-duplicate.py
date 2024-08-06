from typing import List

class Solution:
    """
    A class to solve the 'Contains Duplicate' problem.

    Problem:
        Given an integer array `nums`, return True if any value appears at least twice in the array,
        and return False if every element is distinct.

    Example 1:
        Input: nums = [1,2,3,1]
        Output: True

    Example 2:
        Input: nums = [1,2,3,4]
        Output: False

    Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: True

    Constraints:
        - 1 <= nums.length <= 10^5
        - -10^9 <= nums[i] <= 10^9
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Checks if the input list `nums` contains any duplicates.

        This method works by converting the list to a set, which automatically removes duplicates.
        If the length of the set is less than the length of the list, this indicates that there were duplicates.

        Advantages:
            - Simple and easy to implement.
            - Suitable for small to medium-sized lists where you can afford to process the entire list.

        Disadvantages:
            - The entire list is always processed, even if a duplicate is found early on.
            - May be less efficient in cases where a duplicate appears early in a large list.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            bool: True if there are duplicates, False otherwise.

        Time Complexity:
            O(n): The function involves converting the list to a set, which takes O(n) time,
            where n is the number of elements in the list.

        Space Complexity:
            O(n): The space complexity is O(n) because a set containing up to n elements may need
            to be stored in memory.
        """
        return len(nums) != len(set(nums))

    def containsDuplicateOptimized(self, nums: List[int]) -> bool:
        """
        Checks if the input list `nums` contains any duplicates using an early termination approach.

        This method uses a set to keep track of seen elements as it iterates through the list. If a duplicate
        is found, the function returns True immediately, avoiding the need to process the entire list.

        Advantages:
            - More efficient in practice, especially for large lists where duplicates may be found early.
            - Allows for early termination, potentially saving time.

        Disadvantages:
            - Slightly more complex to implement than the first method.
            - In the worst case (no duplicates), it has the same time complexity as the first method.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            bool: True if there are duplicates, False otherwise.

        Time Complexity:
            O(n): We iterate over the list once, checking for duplicates.

        Space Complexity:
            O(n): We store up to n elements in a set.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    solution = Solution()

    # Define test cases and expected results
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
    ]

    # Loop through the test cases for the original solution
    for nums, expected in test_cases:
        assert solution.containsDuplicate(nums) == expected, f"Test failed for input: {nums}"

    # Loop through the test cases for the optimized solution
    for nums, expected in test_cases:
        assert solution.containsDuplicateOptimized(nums) == expected, f"Test failed for input: {nums}"

    print("All test cases passed!")