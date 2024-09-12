"""
2220. Minimum Bit Flips to Convert Number

Problem Statement:
A bit flip of a number x is choosing a bit in the binary representation of x 
and flipping it from either 0 to 1 or 1 to 0.

Given two integers start and goal, return the minimum number of bit flips 
needed to convert start to goal.

Constraints:
- 0 <= start, goal <= 10^9

Example 1:
    Input: start = 10, goal = 7
    Output: 3
    Explanation: The binary representation of 10 and 7 are 1010 and 0111 
    respectively. We can convert 10 to 7 in 3 steps:
    - Flip the first bit from the right: 1010 -> 1011.
    - Flip the third bit from the right: 1011 -> 1111.
    - Flip the fourth bit from the right: 1111 -> 0111.

Example 2:
    Input: start = 3, goal = 4
    Output: 3
    Explanation: The binary representation of 3 and 4 are 011 and 100 
    respectively. We can convert 3 to 4 in 3 steps:
    - Flip the first bit from the right: 011 -> 010.
    - Flip the second bit from the right: 010 -> 000.
    - Flip the third bit from the right: 000 -> 100.
"""

from typing import List

class Solution:
    """
    Solution class for the 'Minimum Bit Flips to Convert Number' problem.
    """

    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Method 1: Uses manual binary conversion and list comparison to count 
        bit flips.

        Time Complexity:
            O(log(max(start, goal))), where log is base 2. This is because we 
            manually convert both integers to binary, and compare their bits.
        
        Space Complexity:
            O(log(max(start, goal))), for storing the binary representation 
            of both integers.
        
        Args:
            start: An integer representing the start number.
            goal: An integer representing the goal number.
        
        Returns:
            The number of bit flips required to convert start to goal.
        """

        # Helper function to convert an integer to a list of binary digits
        def int2binlist(x: int) -> List[int]:
            ans: List[int] = []
            while x != 0:
                ans.append(x % 2)
                x //= 2
            return ans
        
        # Convert start and goal to binary lists
        startBin: List[int] = int2binlist(start)
        goalBin: List[int] = int2binlist(goal)

        # Pad the shorter binary list with leading zeros
        s: int = len(startBin)
        g: int = len(goalBin)

        while g > s:
            startBin.append(0)
            s += 1
        while s > g:
            goalBin.append(0)
            g += 1

        # Count bit flips
        sol: int = 0  # Initialize counter
        for i in range(s):
            if startBin[i] != goalBin[i]:
                sol += 1

        return sol

    def minBitFlipsOptimized(self, start: int, goal: int) -> int:
        """
        Method 2: Optimized using XOR operation and counting set bits.

        Explanation:
        - The XOR operation gives us a number where each bit is set to 1 if 
          the corresponding bits of the two numbers are different, and 0 if 
          they are the same.
        - We then count the number of set bits (1's) in the XOR result, which 
          gives the number of bit flips required.

        Time Complexity:
            O(log(max(start, goal))), where log is base 2. We perform the XOR 
            operation, then count the number of set bits, which takes time 
            proportional to the number of bits.
        
        Space Complexity:
            O(1), since no extra space is needed except for a few variables.

        Args:
            start: An integer representing the start number.
            goal: An integer representing the goal number.
        
        Returns:
            The number of bit flips required to convert start to goal.
        """
        # XOR start and goal and count the number of 1's in the result
        return bin(start ^ goal).count('1')


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (10, 7, 3),  # Example 1
        (3, 4, 3),   # Example 2
        (8, 8, 0),   # No flips needed
        (1, 0, 1),   # Single bit flip
        (123456, 654321, 11)  # Random case
    ]

    # Instantiate the solution class
    solution = Solution()

    # Run tests for the initial solution
    for i, (start, goal, expected) in enumerate(test_cases):
        result = solution.minBitFlips(start, goal)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    
    print("All manual conversion tests passed!")

    # Run tests for the optimized solution
    for i, (start, goal, expected) in enumerate(test_cases):
        result = solution.minBitFlipsOptimized(start, goal)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    
    print("All optimized solution tests passed!")
