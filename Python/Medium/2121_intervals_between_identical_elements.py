"""
2121. Intervals Between Identical Elements

You are given a 0-indexed array of n integers arr. The interval between two
elements in arr is defined as the absolute difference between their indices.
More formally, the interval between arr[i] and arr[j] is |i - j|.

Return an array intervals of length n where intervals[i] is the sum of
intervals between arr[i] and each element in arr with the same value as
arr[i].

Constraints:
- n == arr.length
- 1 <= n <= 10^5
- 1 <= arr[i] <= 10^5

Note: This question is the same as 2615: Sum of Distances.

Examples:

Example 1:
    Input: arr = [2,1,3,1,2,3,3]
    Output: [4,2,7,2,4,4,5]

Example 2:
    Input: arr = [10,5,10,10]
    Output: [5,0,3,4]
"""

from collections import defaultdict


class Solution:
    def getDistances(self, arr: list[int]) -> list[int]:
        """
        Returns intervals where intervals[i] = sum of |i - j| for all j with
        arr[j] == arr[i].

        Groups indices by value, then for each group uses running prefix sums
        to compute left and right distance contributions in O(1) per element:

            left_distance(i)  = left_count * i - left_sum
            right_distance(i) = right_sum - right_count * i

        where left_sum / right_sum are the sums of indices to the left / right
        of i within the group, and left_count / right_count their cardinalities.

        Time complexity:  O(n) — each index visited once across all groups
        Space complexity: O(n) — index groups and output array
        """
        n = len(arr)
        ans = [0] * n

        num_to_indices: dict[int, list[int]] = defaultdict(list)
        for idx, num in enumerate(arr):
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

                ans[i] = (left_count * i - left_sum) + (right_sum - right_count * i)

                left_sum += i

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 1, 3, 1, 2, 3, 3], [4, 2, 7, 2, 4, 4, 5]),
        ([10, 5, 10, 10], [5, 0, 3, 4]),
        ([1, 1], [1, 1]),
        ([1, 2, 3], [0, 0, 0]),
    ]

    for arr, expected in test_cases:
        result = solution.getDistances(arr)
        assert result == expected, \
            f"getDistances failed: arr={arr} → expected {expected}, got {result}"
    print("All test cases passed!")
