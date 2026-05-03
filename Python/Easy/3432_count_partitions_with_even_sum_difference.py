"""
3432. Count Partitions with Even Sum Difference

You are given an integer array nums of length n.

A partition is defined as an index i where 0 <= i < n - 1, splitting the
array into two non-empty subarrays such that:
  Left subarray contains indices [0, i].
  Right subarray contains indices [i + 1, n - 1].

Return the number of partitions where the difference between the sum of the
left and right subarrays is even.

Constraints:
- 2 <= n == nums.length <= 100
- 1 <= nums[i] <= 100

Examples:

Example 1:
    Input: nums = [10,10,3,7,6]
    Output: 4

Example 2:
    Input: nums = [1,2,2]
    Output: 0

Example 3:
    Input: nums = [2,4,6,8]
    Output: 3
"""


class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        """
        Returns the count of valid partitions using a parity argument.

        For any partition, let L = left sum and S = total sum. Then:
            diff = L - R = L - (S - L) = 2L - S

        Since 2L is always even, the parity of diff depends solely on S:
          - S even  →  2L - S is always even  →  all n-1 partitions are valid
          - S odd   →  2L - S is always odd   →  no partition is valid

        Time complexity:  O(n) to compute the sum
        Space complexity: O(1)
        """
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0

    def countPartitionsLoop(self, nums: list[int]) -> int:
        """
        Returns the count of valid partitions by brute-force enumeration.

        The early exit on odd total avoids the O(n²) loop entirely, since no
        partition can qualify. When the total is even every partition qualifies,
        but the loop still demonstrates the full check.

        Time complexity:  O(n²) due to repeated sum() calls inside the loop
        Space complexity: O(n) for each slice
        """
        if sum(nums) % 2 != 0:
            return 0
        ans: int = 0
        for i in range(len(nums) - 1):
            diff: int = sum(nums[:i]) - sum(nums[i:])
            if diff % 2 == 0:
                ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([10, 10, 3, 7, 6], 4),
        ([1, 2, 2], 0),
        ([2, 4, 6, 8], 3),
        ([1, 1], 1),
        ([1, 2], 0),
    ]

    for label, method in [
        ("countPartitions    ", solution.countPartitions),
        ("countPartitionsLoop", solution.countPartitionsLoop),
    ]:
        for nums, expected in test_cases:
            result = method(nums)
            assert result == expected, \
                f"{label} failed: nums={nums} → expected {expected}, got {result}"
        print(f"  {label} passed")

    print("All test cases passed!")
