"""
2657. Find the Prefix Common Array of Two Arrays

A and B are two 0-indexed permutations of 1..n. Return C where C[i] is the
count of integers present at or before index i in **both** A and B.

Problem Link: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

Examples:
    Example 1:
        Input: A = [1, 3, 2, 4], B = [3, 1, 2, 4]
        Output: [0, 2, 3, 4]

    Example 2:
        Input: A = [2, 3, 1], B = [3, 1, 2]
        Output: [0, 1, 3]

Constraints:
    1 <= A.length == B.length == n <= 50
    1 <= A[i], B[i] <= n
    A and B are permutations of [1..n].
"""


class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        """
        "Seen twice" frequency array. A value v becomes common to both
        prefixes the moment we see it for the second time (once in A, once
        in B — order doesn't matter, since each side is a permutation). One
        counter tracks how many such crossings have occurred.

        Recommended in Python — list-index updates beat the bitmask variant
        (see findThePrefixCommonArrayBitMask docstring for why).

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        n: int = len(A)
        ans: list[int] = [0] * n
        seen: list[int] = [0] * (n + 1)
        counter: int = 0

        for i in range(n):
            seen[A[i]] += 1
            if seen[A[i]] == 2:
                counter += 1

            seen[B[i]] += 1
            if seen[B[i]] == 2:
                counter += 1

            ans[i] = counter

        return ans

    def findThePrefixCommonArrayBitMask(self, A: list[int], B: list[int]) -> list[int]:
        """
        Bitmask intersection. Bit v of maskA flips on once A has seen value
        v; same for maskB. (maskA & maskB).bit_count() is the size of the
        common prefix at step i.

        Algorithmically O(n), but in CPython it is typically *slower* than
        the frequency-array variant: Python ints are heap objects with
        arbitrary precision, so each `1 << A[i]` allocates a new integer
        and each `|=` reallocates the mask. The hardware-register speed of
        bitwise ops that makes this approach shine in Go/C++ is erased by
        the object overhead in Python.

        Time complexity:  O(n) — but with high per-op constants in CPython.
        Space complexity: O(n / word_size) for the masks.
        """
        n: int = len(A)
        ans: list[int] = [0] * n

        maskA = 0
        maskB = 0

        for i in range(n):
            maskA |= (1 << A[i])
            maskB |= (1 << B[i])

            ans[i] = (maskA & maskB).bit_count()

        return ans

    def findThePrefixCommonArraySet(self, A: list[int], B: list[int]) -> list[int]:
        """
        Maintain two growing sets and recompute the intersection size each
        step. Cleanest to read, but the per-step intersection is O(i), so
        total cost is O(n^2). Useful as a baseline / sanity-check.

        Time complexity:  O(n^2)
        Space complexity: O(n)
        """
        n: int = len(A)
        ans: list[int] = [0] * n

        setA: set[int] = set()
        setB: set[int] = set()

        for i in range(n):
            setA.add(A[i])
            setB.add(B[i])
            ans[i] = len(setA.intersection(setB))

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 3, 2, 4], [3, 1, 2, 4], [0, 2, 3, 4]),
        ([2, 3, 1], [3, 1, 2], [0, 1, 3]),
        ([1], [1], [1]),
        ([1, 2], [2, 1], [0, 2]),
    ]

    for i, (A, B, expected) in enumerate(test_cases, 1):
        assert solution.findThePrefixCommonArray(list(A), list(B)) == expected, f"freq test {i} failed"
        assert solution.findThePrefixCommonArrayBitMask(list(A), list(B)) == expected, f"bitmask test {i} failed"
        assert solution.findThePrefixCommonArraySet(list(A), list(B)) == expected, f"set test {i} failed"

    print("All test cases passed!")
