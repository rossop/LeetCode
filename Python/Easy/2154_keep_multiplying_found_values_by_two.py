"""
2154. Keep Multiplying Found Values by Two

Problem Statement:
You are given an array of integers nums and an integer original.

If original is found in nums, multiply it by two (i.e. set original = 2 * original).
Repeat this process with the new number as long as you keep finding it in nums.
Return the final value of original.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i], original <= 1000

Examples:

Example 1:
    Input: nums = [5,3,6,1,12], original = 3
    Output: 24
    Explanation: 3 → 6 → 12 → 24 (24 not in nums, stop).

Example 2:
    Input: nums = [2,7,9], original = 4
    Output: 4
    Explanation: 4 not in nums, return immediately.
"""

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        """
        Returns the final value of original after repeatedly doubling it
        while it exists in nums.

        Searches nums for the current value on each iteration. When the value
        is no longer present, returns it immediately. The bounded constraint
        (nums[i], original <= 1000) limits the number of doublings to at most
        log2(1000) ≈ 10, so the loop runs a constant number of times.

        Args:
            nums (list[int]): The array of integers to search.
            original (int): The starting value to search for and double.

        Returns:
            int: The first value in the doubling sequence not found in nums.

        Time Complexity:
            O(n): Each membership check is O(n) on a list, with at most
            O(log max_val) iterations — effectively O(n) overall.

        Space Complexity:
            O(1): No extra space used.
        """
        num: int = original
        while True:
            if num in nums:
                num *= 2
                continue
            return num


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([5, 3, 6, 1, 12], 3, 24),
        ([2, 7, 9], 4, 4),
    ]

    for i, (nums, original, expected) in enumerate(test_cases, 1):
        result = solution.findFinalValue(nums, original)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed")

    print("All test cases passed!")
