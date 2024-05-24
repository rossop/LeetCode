from typing import List

class Solution:
    """
    Given an integer array nums of size n, return the number with the value 
    closest to 0 in nums. If there are multiple answers, return the number 
    with the largest value.

    

    Example 1:

    Input: nums = [-4,-2,1,4,8]
    Output: 1
    Explanation:
    The distance from -4 to 0 is |-4| = 4.
    The distance from -2 to 0 is |-2| = 2.
    The distance from 1 to 0 is |1| = 1.
    The distance from 4 to 0 is |4| = 4.
    The distance from 8 to 0 is |8| = 8.
    Thus, the closest number to 0 in the array is 1.
    Example 2:

    Input: nums = [2,-1,1]
    Output: 1
    Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
    

    Constraints:

    1 <= n <= 1000
    -105 <= nums[i] <= 105
    """
    def findClosestNumber_v1(self, nums: List[int]) -> int:
        """
        Original solution using a loop with conditionals.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        closest: int = nums[0]
        for num in nums:
            val: int = abs(num)
            if val < abs(closest):
                closest = num
            elif val == abs(closest):
                closest = val if num > closest else closest
        return closest

    def findClosestNumber_map(self, nums: List[int]) -> int:
        """
        Optimized solution using min with a custom key.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        return min(nums, key=lambda x: (abs(x), -x))

    def findClosestNumber_v2(self, nums: List[int]) -> int:
        """
        Solution with a simplified conditional approach.
        Time Complexity: O(n) for the loop + O(n) for the search = O(n + n) = O(2n) = O(n)
        Space Complexity: O(1)
        """
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([-4, -2, 1, 4, 8], 1),
        ([2, -1, 1], 1),
        ([-10, -5, 5, 10], 5),
        ([0, -1, 1], 0),
        ([-2, -3, 3, 2], 2)
    ]
    
    solution = Solution()

    for nums, expected in test_cases:
        assert solution.findClosestNumber_v1(nums) == expected, f"v1 failed on {nums}"
        assert solution.findClosestNumber_map(nums) == expected, f"v2 failed on {nums}"
        assert solution.findClosestNumber_v2(nums) == expected, f"v3 failed on {nums}"
    
    print("All test cases passed!")
