"""
440. K-th Smallest in Lexicographical Order

Problem Statement:
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

Example 1:
    Input: n = 13, k = 2
    Output: 10

Example 2:
    Input: n = 1, k = 1
    Output: 1

Constraints:
- 1 <= k <= n <= 10^9
"""

class Solution:
    """
    This class provides methods to find the k-th lexicographically smallest number
    in the range [1, n].

    Methods:
    1. findKthNumber: Efficient solution using a step-counting approach.
    2. lexicalOrderIterativeVariant: Variant of the iterative lexicographical order generator.
    """

    def findKthNumber(self, n: int, k: int) -> int:
        """
        Efficient approach to find the k-th smallest lexicographical number.
        This approach uses a step-counting method to skip subtrees in the lexicographical
        order tree, improving performance for large inputs.

        Time Complexity: O(log(n) * log(n)), where n is the upper limit.
        Space Complexity: O(1), no extra space other than variables.

        Args:
            n: int - The upper limit of the range.
            k: int - The k-th position in the lexicographical order.

        Returns:
            int - The k-th smallest lexicographically sorted number.
        """
        cur = 1
        k -= 1  # We start with the first number, so decrement k

        def countSteps(n: int, prefix1: int, prefix2: int) -> int:
            """
            Helper function to count the steps between two prefixes in the lexicographical order.
            
            Args:
                n: int - The upper limit of the range.
                prefix1: int - The current prefix.
                prefix2: int - The next prefix to count up to.

            Returns:
                int - The number of steps between prefix1 and prefix2.
            """
            steps = 0
            while prefix1 <= n:
                steps += min(n + 1, prefix2) - prefix1
                prefix1 *= 10
                prefix2 *= 10
            return steps

        while k > 0:
            step = countSteps(n, cur, cur + 1)
            if step <= k:
                cur += 1  # Move to the next sibling in the lexicographical tree
                k -= step
            else:
                cur *= 10  # Move to the first child in the subtree
                k -= 1

        return cur

    def lexicalOrderIterativeVariant(self, n: int, k: int) -> int:
        """
        Iterative approach to lexicographically generate numbers and find the k-th smallest one.
        This method can encounter issues with memory or time limits for very large inputs.

        Time Complexity: O(n), where n is the total number of integers to generate.
        Space Complexity: O(n), due to the space used to store the numbers.

        Note: This method works for small `n` but is not efficient for very large values of `n`.

        Args:
            n: int - The upper limit of the range.
            k: int - The k-th position in the lexicographical order.

        Returns:
            int - The k-th smallest lexicographically sorted number.
        """
        res = []
        cur = 1
        while len(res) < k:
            res.append(cur)

            if cur * 10 <= n:
                cur *= 10
            else:
                while cur == n or cur % 10 == 9:
                    cur //= 10
                cur += 1

        return res[k - 1]


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        (13, 2, 10),
        (1, 1, 1),
        (100, 10, 17),
        (1000, 500, 548),
    ]

    solution = Solution()

    # Test the lexicalOrderIterativeVariant method (Not recommended for large inputs)
    print("\nTesting lexicalOrderIterativeVariant (Variant):")
    for i, (n, k, expected) in enumerate(test_cases[:2]):  # Only testing small cases
        result = solution.lexicalOrderIterativeVariant(n, k)
        assert result == expected, f"Test case {i+1} failed (Variant): Expected {expected}, but got {result}"
    print("All test cases passed for lexicalOrderIterativeVariant!")

    # Add test cases that won;t work on iterative solution
    test_cases.append((804289384, 42641503, 138377349)) # Memory 
    test_cases.append((681692778, 351251360, 416126219)) # Time limit

    # Test the efficient findKthNumber method
    print("Testing findKthNumber (Efficient):")
    for i, (n, k, expected) in enumerate(test_cases):
        result = solution.findKthNumber(n, k)
        assert result == expected, f"Test case {i+1} failed (Efficient): Expected {expected}, but got {result}"
    print("All test cases passed for findKthNumber!")
