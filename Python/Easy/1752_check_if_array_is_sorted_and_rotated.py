"""
1752. Check if Array Is Sorted and Rotated

Return true if nums could have been produced by rotating a non-decreasing
array (rotation by 0 counts). Duplicates allowed.

Problem Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

Examples:
    Example 1:
        Input: nums = [3, 4, 5, 1, 2]
        Output: true

    Example 2:
        Input: nums = [2, 1, 3, 4]
        Output: false

    Example 3:
        Input: nums = [1, 2, 3]
        Output: true

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""


class Solution:
    def check(self, nums: list[int]) -> bool:
        """
        Walk the array as if it were circular: visit each pair (i, i+1) for
        i in 0..2n-1 using modular indexing. Track the longest run of
        non-decreasing steps — on a drop, reset to 1. If any run reaches n,
        the array is a rotation of a sorted sequence.

        Why 2n? Crossing the rotation pivot can be anywhere; walking around
        twice guarantees the full n-length non-decreasing run is seen
        regardless of where it starts.

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        N: int = len(nums)

        count: int = 1
        for idx in range(1, 2 * N):
            if nums[idx % N - 1] > nums[idx % N]:
                count = 1
            else:
                count += 1
            if count == N:
                return True
        return N == 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 4, 5, 1, 2], True),
        ([2, 1, 3, 4], False),
        ([1, 2, 3], True),
        ([1], True),
        ([1, 1, 1], True),
        ([7, 9, 1, 1, 1], True),
        ([2, 1], True),
        ([6, 10, 6], True),
        ([2, 4, 1, 3], False),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.check(list(nums)) == expected, f"check test {i} failed: {nums} → expected {expected}"

    print("All test cases passed!")
