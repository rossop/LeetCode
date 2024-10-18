"""
845. Longest Mountain in Array

Problem Statement:
You may recall that an array arr is a mountain array if and only if:
- arr.length >= 3
- There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ...
    > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which
is a mountain. Return 0 if there is no mountain subarray.

Examples:
Example 1:
    Input: arr = [2, 1, 4, 7, 3, 2, 5]
    Output: 5
    Explanation: The largest mountain is [1, 4, 7, 3, 2] which has length 5.

Example 2:
    Input: arr = [2, 2, 2]
    Output: 0
    Explanation: There is no mountain.

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^4

Follow up:
- Can you solve it using only one pass?
- Can you solve it in O(1) space?
"""
from typing import List


class Solution:
    """
    This class provides multiple methods to solve the Longest Mountain problem.
    Each method uses a different approach to find the longest mountain.
    """

    def longestMountain(self, arr: List[int]) -> int:
        """
        Original solution that tracks valleys and peaks to find the longest
        mountain.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Args:
            arr (List[int]): List of integers representing the array.

        Returns:
            int: Length of the longest mountain.
        """
        n: int = len(arr)
        if n <= 2:
            return 0

        valleys: List[int] = []
        peaks: List[int] = []
        dist: int = 0

        for i in range(n):
            if i == 0:
                if arr[i + 1] > arr[i]:
                    valleys.append(i)
                elif arr[i + 1] < arr[i]:
                    peaks.append(i)
            elif i == n - 1:
                if arr[i - 1] > arr[i]:
                    valleys.append(i)
                elif arr[i - 1] < arr[i]:
                    peaks.append(i)
            else:
                if arr[i - 1] >= arr[i] <= arr[i + 1]:
                    valleys.append(i)
                if arr[i - 1] < arr[i] >= arr[i + 1]:
                    peaks.append(i)

            if len(valleys) >= 2 and len(peaks) >= 1:
                unique_up: bool = len(set(arr[valleys[-2]:peaks[-1] + 1])) == \
                    len(arr[valleys[-2]:peaks[-1] + 1])
                unique_down: bool = len(set(arr[peaks[-1]:valleys[-1] + 1])) \
                    == len(arr[peaks[-1]:valleys[-1] + 1])

                if unique_up and unique_down:
                    dist = max(valleys[-1] - valleys[-2], dist)

        return dist + 1 if dist > 0 else 0

    def longestMountainBruteForce(self, arr: List[int]) -> int:
        """
        Brute force solution that checks for mountains at each index.

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Args:
            arr (List[int]): List of integers representing the array.

        Returns:
            int: Length of the longest mountain.
        """
        n: int = len(arr)
        longest_mountain: int = 0

        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left: int = i - 1
                right: int = i + 1

                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                while right < n - 1 and arr[right + 1] < arr[right]:
                    right += 1

                mountain_len: int = right - left + 1
                longest_mountain = max(longest_mountain, mountain_len)

        return longest_mountain

    def longestMountainRecommended(self, arr: List[int]) -> int:
        """
        Efficient recommended solution that finds the longest mountain in one
        pass.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            arr (List[int]): List of integers representing the array.

        Returns:
            int: Length of the longest mountain.
        """
        n: int = len(arr)
        base: int = 0
        ans: int = 0

        while base < n:
            end: int = base
            if end + 1 < n and arr[end] < arr[end + 1]:  # Left boundary
                while end + 1 < n and arr[end] < arr[end + 1]:  # Reach peak
                    end += 1

                if end + 1 < n and arr[end] > arr[end + 1]:  # Right boundary
                    while end + 1 < n and arr[end] > arr[end + 1]:
                        end += 1
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    arr1: List[int] = [2, 1, 4, 7, 3, 2, 5]
    assert solution.longestMountain(arr1) == 5
    assert solution.longestMountainBruteForce(arr1) == 5
    assert solution.longestMountainRecommended(arr1) == 5

    # Test Case 2
    arr2: List[int] = [2, 2, 2]
    assert solution.longestMountain(arr2) == 0
    assert solution.longestMountainBruteForce(arr2) == 0
    assert solution.longestMountainRecommended(arr2) == 0

    # Test Case 3
    arr3: List[int] = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    assert solution.longestMountain(arr3) == 11
    assert solution.longestMountainBruteForce(arr3) == 11
    assert solution.longestMountainRecommended(arr3) == 11

    # Test Case 4
    arr4: List[int] = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert solution.longestMountain(arr4) == 0
    assert solution.longestMountainBruteForce(arr4) == 0
    assert solution.longestMountainRecommended(arr4) == 0

    # Test Case 5
    arr5: List[int] = [0, 2, 0, 2, 1, 2, 3, 4, 4, 1]
    assert solution.longestMountain(arr5) == 3
    assert solution.longestMountainBruteForce(arr5) == 3
    assert solution.longestMountainRecommended(arr5) == 3

    # Test Case 6
    arr6: List[int] = [1, 1, 0, 0, 1, 0]
    assert solution.longestMountain(arr6) == 3
    assert solution.longestMountainBruteForce(arr6) == 3
    assert solution.longestMountainRecommended(arr6) == 3

    print("All test cases passed!")
