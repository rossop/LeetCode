from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Calculates the maximum amount of water a container can store, formed by 
        two vertical lines from the input list `height` and the x-axis.

        The container's capacity is determined by the shorter of the two heights, 
        multiplied by the distance between them. This method uses a two-pointer 
        approach to find the maximum possible area efficiently.

        Args:
            height (List[int]): A list of integers representing the height of the vertical lines.

        Returns:
            int: The maximum amount of water a container can store.

        Time Complexity:
            O(n): The algorithm iterates over the list once using two pointers.

        Space Complexity:
            O(1): No additional space is used beyond a few variables.

        Example:
            Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
            Output: 49
            Explanation: The maximum area is between lines 8 and 7, with a width of 7 units.

        Constraints:
            - 2 <= height.length <= 10^5
            - 0 <= height[i] <= 10^4
        """
        n = len(height)
        L: int = 0
        R: int = n - 1

        water = 0

        while L < R:
            # Calculate the area with the current left and right pointers
            val = min(height[L], height[R]) * (R - L)
            if val > water:
                water = val
            
            # Move the pointers
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1

        return water

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1, 3, 2, 5, 25, 24, 5], 24)
    ]

    # Run the test cases
    for i, (height, expected) in enumerate(test_cases):
        result = solution.maxArea(height)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases passed!")