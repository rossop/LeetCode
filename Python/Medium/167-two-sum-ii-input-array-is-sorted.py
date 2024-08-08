from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers in the sorted array `numbers` that add up to the `target`.
        
        The function uses a two-pointer approach to find the indices of the two numbers that sum up 
        to the target. Since the array is sorted, it starts with pointers at the beginning (L) 
        and end (R) of the array and moves them towards the center until the sum of the elements 
        at these pointers equals the target.

        Args:
            numbers (List[int]): A list of integers sorted in non-decreasing order.
            target (int): The target sum to find.

        Returns:
            List[int]: A list containing the 1-indexed positions of the two numbers that add up to the target.

        Time Complexity:
            O(n): The array is traversed at most once, making this an O(n) solution.

        Space Complexity:
            O(1): The solution uses constant extra space.

        Example:
            Input: numbers = [2, 7, 11, 15], target = 9
            Output: [1, 2]
            Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
        
        Constraints:
            - The array `numbers` is sorted in non-decreasing order.
            - There is exactly one solution, and you may not use the same element twice.
            - The length of `numbers` is between 2 and 10^4.
        """
        n = len(numbers)
        L: int = 0
        R: int = n - 1

        while L < R:
            summ = numbers[L] + numbers[R]
            if summ > target:
                R -= 1
            elif summ < target:
                L += 1
            else:
                return [L + 1, R + 1]

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5])
    ]

    # Run and validate the test cases
    for i, (numbers, target, expected) in enumerate(test_cases):
        result = solution.twoSum(numbers, target)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases passed!")