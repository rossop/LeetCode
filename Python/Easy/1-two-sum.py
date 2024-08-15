from typing import Dict, List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in `nums` that sum up to `target` and returns their indices.

        This method uses a hash map (dictionary) to store each number's index as we iterate 
        through the list. For each number, it checks if the complement (target - current number) 
        exists in the dictionary. If it does, the indices of the current number and its complement 
        are returned.

        Time Complexity:
            O(n): The list is traversed once, making the time complexity linear.
        
        Space Complexity:
            O(n): The space complexity is linear because the dictionary stores up to n elements.

        Args:
            nums (List[int]): The list of integers.
            target (int): The target sum for two numbers in `nums`.

        Returns:
            List[int]: The indices of the two numbers that sum up to `target`.
        """
        lookup: Dict[int,int] = {}
        for i, num in enumerate(nums):
            complement: int = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
        return []  # This line will never be reached because the problem guarantees one solution.

if __name__ == '__main__':
    solution = Solution()

    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),  # Example 1
        ([3, 2, 4], 6, [1, 2]),       # Example 2
        ([3, 3], 6, [0, 1]),          # Example 3
        ([1, 2, 3, 4], 7, [2, 3]),    # Additional case
        ([2, 5, 5, 11], 10, [1, 2])   # Case with duplicate numbers
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = solution.twoSum(nums, target)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases passed!")