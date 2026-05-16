"""
1470. Shuffle the Array

Given nums of length 2n in the form [x1, x2, ..., xn, y1, y2, ..., yn], return
[x1, y1, x2, y2, ..., xn, yn].

Problem Link: https://leetcode.com/problems/shuffle-the-array/

Examples:
    Example 1:
        Input: nums = [2, 5, 1, 3, 4, 7], n = 3
        Output: [2, 3, 5, 4, 1, 7]

    Example 2:
        Input: nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4
        Output: [1, 4, 2, 3, 3, 2, 4, 1]

    Example 3:
        Input: nums = [1, 1, 2, 2], n = 2
        Output: [1, 2, 1, 2]

Constraints:
    1 <= n <= 500
    nums.length == 2n
    1 <= nums[i] <= 10^3
"""


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        """
        Walk i from 0 to n-1 and append the matching x_i and y_i (= nums[n+i])
        side by side. Simplest reading of the spec.

        Time complexity:  O(n)
        Space complexity: O(n) — for the output array.
        """
        ans: list[int] = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n + i])
        return ans

    def shufflePrefilled(self, nums: list[int], n: int) -> list[int]:
        """
        Pre-allocate the 2n result and fill by parity: even slots take from
        the x half, odd slots take from the y half. Useful when the output
        size is known and append overhead matters.

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        ans: list[int] = [0] * (2 * n)
        for i in range(2 * n):
            if i % 2 == 0:
                ans[i] = nums[i // 2]
            else:
                ans[i] = nums[n + i // 2]
        return ans

    def shuffleZip(self, nums: list[int], n: int) -> list[int]:
        """
        Slice nums into its x and y halves, then zip them so each (x, y) pair
        is produced together. Pythonic but allocates two intermediate slices.

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        ans: list[int] = []
        for x, y in zip(nums[:n], nums[n:]):
            ans.append(x)
            ans.append(y)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
        ([1, 2, 3, 4], 2, [1, 3, 2, 4]),
        ([10, 20, 30, 40, 50, 60], 3, [10, 40, 20, 50, 30, 60]),
    ]

    for k, (nums, n, expected) in enumerate(test_cases, 1):
        assert solution.shuffle(list(nums), n) == expected, f"shuffle test {k} failed"
        assert solution.shufflePrefilled(list(nums), n) == expected, f"shufflePrefilled test {k} failed"
        assert solution.shuffleZip(list(nums), n) == expected, f"shuffleZip test {k} failed"

    print("All test cases passed!")
