from typing import List

class Solution:
    def trapOptimised(self, height: List[int]) -> int:
        """
        Calculate the total amount of water trapped using precomputed maximum heights 
        from the left and right of each element.

        This method uses two arrays (`max_left` and `max_right`) to store the maximum 
        height to the left and right of each bar. By precomputing these values, the 
        method calculates the trapped water in a single pass.

        Args:
            height (List[int]): A list of integers representing the elevation map.

        Returns:
            int: The total amount of water trapped.

        Time Complexity:
            O(n): We traverse the height array three times (one for `max_left`, one for 
            `max_right`, and one to calculate the trapped water).

        Space Complexity:
            O(n): Two extra arrays of size `n` are used to store the maximum heights.

        Comparison:
            - This method is more space-intensive than the `trap` and `trapTwoPointers` methods 
              due to the additional arrays.
            - It is straightforward and easy to understand, especially for those new to the problem.
        """
        n: int = len(height)
        max_left: List[int] = [0] * n
        max_right: List[int] = [0] * n
        left_wall = 0
        right_wall = 0

        water: int = 0

        for i in range(n):
            j = -i - 1
            max_left[i] = left_wall
            max_right[j] = right_wall

            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])
        
        for i in range(n):
            potential = min(max_left[i], max_right[i])
            water += max(0, potential - height[i])

        return water

    def trapTwoPointers(self, height: List[int]) -> int:
        """
        Calculate the total amount of water trapped using a two-pointer approach 
        that finds valleys between peaks.

        This method uses two pointers (`topL` and `topR`) that move towards each other, 
        identifying peaks and valleys where water can be trapped. It first processes 
        from the left to the right, then from the right to the left.

        Args:
            height (List[int]): A list of integers representing the elevation map.

        Returns:
            int: The total amount of water trapped.

        Time Complexity:
            O(n): We traverse the height array twice (once from left to right, once from right to left).

        Space Complexity:
            O(1): Only a few extra variables are used.

        Comparison:
            - This method is more space-efficient than `trapOptimised` since it does not use extra arrays.
            - It requires careful pointer management and may be harder to understand at first.
            - It is similar in efficiency to the `trap` method but takes a different approach.
        """
        n: int = len(height)
        if n == 0:
            return 0

        topL: int = 0  # Left pointer, starts at the first bar
        water: int = 0

        for pos in range(1, n):
            if height[pos] >= height[topL]:
                for i in range(topL + 1, pos):
                    water += max(0, height[topL] - height[i])
                topL = pos

        topR = n - 1
        for pos in range(n - 2, topL - 1, -1):
            if height[pos] >= height[topR]:
                for i in range(topR - 1, pos, -1):
                    water += max(0, height[topR] - height[i])
                topR = pos

        return water
    
    def trap(self, height: List[int]) -> int:
        """
        Calculate the total amount of water trapped using a two-pointer technique that 
        dynamically calculates the maximum height seen from both the left and the right.

        This method uses two pointers (`left` and `right`) to scan the elevation map 
        from both ends towards the center. It dynamically updates the maximum heights 
        seen so far and calculates the trapped water accordingly.

        Args:
            height (List[int]): A list of integers representing the elevation map.

        Returns:
            int: The total amount of water trapped.

        Time Complexity:
            O(n): We traverse the height array only once.

        Space Complexity:
            O(1): Only a few extra variables are used.

        Comparison:
            - This method is the most efficient in terms of both time and space.
            - It is intuitive once the concept of dynamically updating the maximum heights 
              is understood.
            - It combines the simplicity of the two-pointer technique with the efficiency 
              of dynamic updates.
        """
        if not height:
            return 0

        left: int = 0
        right: int = len(height) - 1
        left_max: int = height[left]
        right_max: int = height[right]
        water: int = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += max(0, right_max - height[right])

        return water
    

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([3, 0, 1, 3, 0, 5], 8),
        ([2, 1, 0, 2], 3),
        ([0, 0, 0, 0], 0),
        ([1, 7, 8], 0),
        ([5, 2, 1, 2, 1, 5], 14),
        ([4, 4, 4, 4, 4], 0)
    ]

    # Run the test cases for all three methods
    for i, (height, expected) in enumerate(test_cases):
        result_optimised = solution.trapOptimised(height.copy())
        result_two_pointers = solution.trapTwoPointers(height.copy())
        result_standard = solution.trap(height.copy())
        
        assert result_optimised == expected, f"Optimised Test case {i+1} failed: expected {expected}, got {result_optimised}"
        assert result_two_pointers == expected, f"Two Pointers Test case {i+1} failed: expected {expected}, got {result_two_pointers}"
        assert result_standard == expected, f"Standard Test case {i+1} failed: expected {expected}, got {result_standard}"

    print("All test cases passed!")