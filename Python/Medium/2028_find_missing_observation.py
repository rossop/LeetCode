"""
2028. Find Missing Observations

You have observations of n + m 6-sided dice rolls with each face numbered from
1 to 6. n of the observations went missing, and you only have the observations
of m rolls. Fortunately, you have also calculated the average value of the
n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of
the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the
average value of the n + m rolls is exactly mean. If there are multiple valid
answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible
by n + m.

Example 1: Input: rolls = [3,2,4,3], mean = 4, n = 2 Output: [6,6] Explanation:
The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

Example 2: Input: rolls = [1,5,6], mean = 3, n = 4 Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is
(1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.

Example 3: Input: rolls = [1,2,3,4], mean = 6, n = 4 Output: [] Explanation: It
is impossible for the mean to be 6 no matter what the 4 missing rolls are.

Constraints: - m == rolls.length - 1 <= n, m <= 105 - 1 <= rolls[i], mean <= 6
"""

from typing import List


class Solution:
    """
    This class provides two methods to solve the '2028. Find Missing
    Observations' problem.

    Method 1 uses a straightforward approach to calculate the missing
    observations, while Method 2 uses a more efficient approach.

    Time Complexity for both methods: O(m + n), where m is the length of the
    rolls array and n is the number of missing observations. Space Complexity:
    O(n) to store the result list of missing observations.
    """

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        Determines the missing observations such that the total mean of the
        combined rolls equals the target mean.

        Args:
            rolls (List[int]): List of observed dice rolls. mean (int): Target
            mean for the total n + m rolls. n (int): Number of missing
            observations.

        Returns:
            List[int]: A list of missing observations if possible, or an empty
            list if not.

        Time Complexity: O(m + n) where m is the length of rolls, and n is the
        number of missing observations. Space Complexity: O(n) to store the
        missing observations.
        """
        m: int = len(rolls)
        total_observations: int = m + n
        sum_of_observations: int = mean * total_observations
        sum_of_given_dice_rolls: int = sum(rolls)
        remaining_sum: int = sum_of_observations - sum_of_given_dice_rolls

        # Edge conditions: Check if the remaining sum is achievable
        if remaining_sum > 6 * n or remaining_sum < n:
            return []

        # Distribute the remaining sum evenly across n missing rolls
        distribute_mean = remaining_sum // n
        mod = remaining_sum % n

        # Create a list with the base value and distribute the remainder
        n_elements = [distribute_mean] * n
        for i in range(mod):
            n_elements[i] += 1

        return n_elements

    def missingRollsOptimized(
                             self, rolls: List[int],
                             mean: int, n: int) -> List[int]:
        """
        Optimized approach to determine the missing observations by directly
        computing the missing sum and distributing it with minimal iterations.

        Args:
            rolls (List[int]): List of observed dice rolls. mean (int): Target
            mean for the total n + m rolls. n (int): Number of missing
            observations.

        Returns:
            List[int]: A list of missing observations if possible, or an empty
            list if not.

        Time Complexity: O(m + n) where m is the length of rolls, and n is the
        number of missing observations. Space Complexity: O(n) to store the
        missing observations.
        """
        # Calculate the total number of rolls and
        # the remaining sum required for missing rolls
        m: int = len(rolls)
        total_sum_needed: int = mean * (m + n)
        sum_given: int = sum(rolls)
        remaining_sum: int = total_sum_needed - sum_given

        # If the remaining sum is not feasible, return an empty list
        if remaining_sum > 6 * n or remaining_sum < n:
            return []

        # Create a list to store the missing rolls,
        # distributing the remainder as evenly as possible
        quotient, remainder = divmod(remaining_sum, n)
        missing_rolls = [quotient + 1] * remainder + [quotient] * (n - remainder)

        return missing_rolls


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([3, 2, 4, 3], 4, 2, [6, 6]),  # Example 1
        ([1, 5, 6], 3, 4, [3, 2, 2, 2]),  # Example 2
        ([1, 2, 3, 4], 6, 4, []),  # Example 3
        ([2, 3], 3, 3, [4, 3, 3]),  # Additional test case 1
        ([6, 3, 5], 5, 2, [6, 5]),  # Additional test case 2
    ]

    solution = Solution()

    # Run the test cases
    for i, (rolls, mean, n, expected) in enumerate(test_cases):
        result = solution.missingRolls(rolls, mean, n)
        assert result == expected, f"missingRolls test case {i+1} failed: Expected {expected}, but got {result}"

        # Testing optimized version
        result_optimized = solution.missingRollsOptimized(rolls, mean, n)
        assert result_optimized == expected, f"missingRollsOptimized test case {i+1} failed: Expected {expected}, but got {result_optimized}"

    print("All test cases passed!")
