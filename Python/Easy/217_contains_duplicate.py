"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Examples:

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Returns True if any value appears at least twice.

        Converts nums to a set, discarding duplicates. If the set is smaller
        than the original list, at least one duplicate exists. Always processes
        the entire list.

        Time complexity:  O(n)
        Space complexity: O(n) for the set
        """
        return len(set(nums)) != len(nums)

    def containsDuplicateEarlyExit(self, nums: list[int]) -> bool:
        """
        Returns True if any value appears at least twice, with early exit.

        Iterates once, inserting each element into a seen set. Returns True
        immediately on the first repeated element, avoiding unnecessary work
        when a duplicate appears early in a large list.

        Time complexity:  O(n) worst case; faster in practice with early exit
        Space complexity: O(n) for the seen set
        """
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([1], False),
    ]

    for label, method in [
        ("containsDuplicate         ", solution.containsDuplicate),
        ("containsDuplicateEarlyExit", solution.containsDuplicateEarlyExit),
    ]:
        for nums, expected in test_cases:
            result = method(nums)
            assert result == expected, \
                f"{label} failed: nums={nums} → expected {expected}, got {result}"
        print(f"  {label} passed")

    print("All test cases passed!")
