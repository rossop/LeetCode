"""
1299. Replace Elements with Greatest Element on Right Side

Replace every arr[i] with max(arr[i+1..n-1]); the last element becomes -1.

Problem Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Examples:
    Example 1:
        Input: arr = [2, 4, 5, 3, 1, 2]
        Output: [5, 5, 3, 2, 2, -1]

    Example 2:
        Input: arr = [3, 3]
        Output: [3, -1]

Constraints:
    1 <= arr.length <= 10_000
    1 <= arr[i] <= 100_000
"""


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        """
        Walk right-to-left holding rightMax — the max of everything strictly
        to the right of i. Swap arr[i] with rightMax in one move, then fold
        the original value into rightMax for the next step. Initial value
        -1 satisfies the "last element becomes -1" rule for free.

        Time complexity:  O(n)
        Space complexity: O(1) — in place.
        """
        rightMax: int = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax: int = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr

    def replaceElementsLeftToRight(self, arr: list[int]) -> list[int]:
        """
        Brute force: for each i scan the suffix arr[i+1..] for its max. Easy
        to reason about, but n nested scans push runtime to O(n^2).

        Time complexity:  O(n^2)
        Space complexity: O(1) — in place.
        """
        n: int = len(arr)
        if n == 0:
            return arr

        for i in range(n - 1):
            arr[i] = max(arr[i + 1:])

        arr[n - 1] = -1
        return arr


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 4, 5, 3, 1, 2], [5, 5, 3, 2, 2, -1]),
        ([3, 3], [3, -1]),
        ([400], [-1]),
        ([1, 2, 3, 4, 5], [5, 5, 5, 5, -1]),
        ([5, 4, 3, 2, 1], [4, 3, 2, 1, -1]),
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        assert solution.replaceElements(list(arr)) == expected, f"replaceElements test {i} failed"
        assert solution.replaceElementsLeftToRight(list(arr)) == expected, f"replaceElementsLeftToRight test {i} failed"

    print("All test cases passed!")
