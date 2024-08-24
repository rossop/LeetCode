"""
2433. Find The Original Array of Prefix Xor

You are given an integer array pref of size n. Find and return the array arr of
size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].

Note that ^ denotes the bitwise-XOR operation.

It can be proven that the answer is unique.

Example 1:

Input: pref = [5, 2, 0, 3, 1]
Output: [5, 7, 2, 3, 2]
Explanation:
From the array [5, 7, 2, 3, 2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

Example 2:

Input: pref = [13]
Output: [13]
Explanation: We have pref[0] = arr[0] = 13.

Constraints:
- 1 <= pref.length <= 10^5
- 0 <= pref[i] <= 10^6
"""
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """
        Find the original array from the prefix XOR array using an optimized
        approach.

        Args:
            pref (List[int]): A list of integers representing the prefix XOR
            values.

        Returns:
            List[int]: The original array that corresponds to the given prefix
            XOR array.

        Time Complexity: O(n)
            - We traverse the list once, performing O(1) operations at each
            step.
        Space Complexity: O(n)
            - We use an additional array to store the result, so the space
            complexity is linear.
        """
        n: int = len(pref)
        arr: List[int] = [0] * n
        arr[0] = pref[0]

        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i - 1]

        return arr

    def findArrayBruteForce(self, pref: List[int]) -> List[int]:
        """
        Find the original array from the prefix XOR array using a brute-force
        approach.

        This method is less efficient because it recalculates the XOR sum for
        each element in the array.

        Args:
            pref (List[int]): A list of integers representing the prefix XOR
            values.

        Returns:
            List[int]: The original array that corresponds to the given prefix
            XOR array.

        Time Complexity: O(n^2)
            - We perform a nested loop, where for each element, we iterate over
            the entire array.
        Space Complexity: O(n)
            - We use an additional array to store the result, so the space
            complexity is linear.
        """
        n: int = len(pref)
        arr: List[int] = []
        curr: int = 0

        for i in range(n):
            curr = pref[i]
            for a in arr:
                curr ^= a
            arr.append(curr)

        return arr


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (Input, Expected Output)
        ([5, 2, 0, 3, 1], [5, 7, 2, 3, 2]),
        ([13], [13]),
        ([1, 3, 7, 15], [1, 2, 4, 8]),
        ([2, 3, 6, 14, 28], [2, 1, 5, 8, 18])
    ]

    for k, (prefList, expected) in enumerate(test_cases):
        assert solution.findArray(prefList) == expected, f"""
        Test case {k + 1} failed for optimized solution."""
        assert solution.findArrayBruteForce(prefList) == expected, f"""
        Test case {k + 1} failed for brute-force solution."""

    print("All tests passed!")
