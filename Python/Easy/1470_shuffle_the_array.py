"""
1470. Shuffle the Array
https://leetcode.com/problems/shuffle-the-array/

Given the array nums consisting of 2n elements in the form
[x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7
then the answer is [2,3,5,4,1,7].

Example 2:
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

Constraints:
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
"""

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Shuffle the array into the format [x1,y1,x2,y2,...,xn,yn].

        Args:
        nums (List[int]): The input array containing 2n elements.
        n (int): The number of pairs.

        Returns:
        List[int]: The shuffled array.

        Time Complexity: O(n)
        Space Complexity: O(1) (excluding the output list)
        """
        ans: List[int] = [0] * (2 * n)
        left: int = 0
        right: int = n
        i: int = 0
        while left < n:
            ans[i] = nums[left]
            ans[i + 1] = nums[right]
            left += 1
            right += 1
            i += 2
        return ans


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
        ([1, 2, 3, 4], 2, [1, 3, 2, 4]),
        ([10, 20, 30, 40, 50, 60], 3, [10, 40, 20, 50, 30, 60])
    ]

    for k, (numbers, n, expected) in enumerate(test_cases):
        result = solution.shuffle(numbers, n)
        assert result == expected, f"""
        Test case {k+1} failed: expected {expected}, got {result}"""

    print("All test cases passed!")
