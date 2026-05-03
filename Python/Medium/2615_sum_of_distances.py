"""
2615. Sum of Distances

You are given a 0-indexed integer array nums. There exists an array arr of
length nums.length, where arr[i] is the sum of |i - j| over all j such that
nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to 0.

Return the array arr.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9

Note: This question is the same as 2121: Intervals Between Identical Elements.

Examples:

Example 1:
    Input: nums = [1,3,1,1,2]
    Output: [5,0,3,4,0]

Example 2:
    Input: nums = [0,5,3]
    Output: [0,0,0]
"""

from collections import defaultdict


class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        """
        Returns arr where arr[i] = sum of |i - j| for all j with nums[j] == nums[i].

        Groups indices by value, then for each group uses running prefix sums
        to compute left and right distance contributions in O(1) per element:

            left_distance(i)  = left_count * i - left_sum
            right_distance(i) = right_sum - right_count * i

        where left_sum / right_sum are the sums of indices to the left / right
        of i within the group, and left_count / right_count their cardinalities.

        Time complexity:  O(n) — each index visited once across all groups
        Space complexity: O(n) — index groups and output array
        """
        n = len(nums)
        arr = [0] * n

        num_to_indices: dict[int, list[int]] = defaultdict(list)
        for idx, num in enumerate(nums):
            num_to_indices[num].append(idx)

        for indices in num_to_indices.values():
            k = len(indices)
            if k <= 1:
                continue

            total_sum = sum(indices)
            left_sum = 0

            for m, i in enumerate(indices):
                right_sum = total_sum - left_sum - i
                left_count = m
                right_count = k - 1 - m

                arr[i] = (left_count * i - left_sum) + (right_sum - right_count * i)

                left_sum += i

        return arr


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 3, 1, 1, 2], [5, 0, 3, 4, 0]),
        ([0, 5, 3], [0, 0, 0]),
        ([1, 1], [1, 1]),
        ([1, 1, 1], [3, 2, 3]),
    ]

    for nums, expected in test_cases:
        result = solution.distance(nums)
        assert result == expected, \
            f"distance failed: nums={nums} → expected {expected}, got {result}"
    print("All test cases passed!")
