"""
539. Minimum Time Difference

Problem Statement: Given a list of 24-hour clock time points in "HH:MM" format,
return the minimum minutes difference between any two time-points in the list.

Example 1: Input: timePoints = ["23:59", "00:00"] Output: 1

Example 2: Input: timePoints = ["00:00", "23:59", "00:00"] Output: 0

Constraints: - 2 <= timePoints.length <= 2 * 10^4 - timePoints[i] is in the
format "HH:MM".
"""

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        This method finds the minimum time difference between two time points
        by converting the time into minutes and then computing the difference.

        Time Complexity: O(n log n) - The timePoints list is sorted, and then
            we traverse the list once to calculate differences.
        Space Complexity: O(n) - We store the time in minutes and use 
            additional helper lists for conversions.

        Args:
            timePoints: A list of strings representing time in "HH:MM" format.

        Returns:
            int: The minimum time difference in minutes.
        """
        if not timePoints:
            return 0

        # Sort the time points
        timePoints.sort()

        # Helper function to convert time string to minutes
        def convert2min(t: str) -> int:
            hours, minutes = map(int, t.split(":"))
            return hours * 60 + minutes

        # Helper function to return the minimum time difference for circular times
        def returnMinTime(t: int) -> int:
            return min(t, 1440 - t)

        n = len(timePoints)
        ansMin = float("inf")

        # Calculate the difference between the first and last times to handle circular case
        ans = abs(convert2min(timePoints[-1]) - convert2min(timePoints[0]))
        ansMin = min(returnMinTime(ans), ansMin)

        # Loop through each pair of adjacent times
        for i in range(n - 1):
            ans = abs(convert2min(timePoints[i + 1]) - convert2min(timePoints[i]))
            ansMin = min(returnMinTime(ans), ansMin)

        return ansMin

    def findMinDifferenceOptimized(self, timePoints: List[str]) -> int:
        """
        Optimized method using the same approach but with a more direct approach without requiring 
        the additional helper function for circular cases.

        Time Complexity: O(n log n) - The timePoints list is sorted, and we compute differences.
        Space Complexity: O(1) - Aside from the input and a few variables, no additional space is used.

        Args:
            timePoints: A list of strings representing time in "HH:MM" format.

        Returns:
            int: The minimum time difference in minutes.
        """
        if len(timePoints) > 1440:  # If there are more than 1440 times, there must be a duplicate
            return 0

        # Sort the time points
        timePoints.sort()

        # Convert times into minutes
        minutes = list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), timePoints))

        # Initialize the minimum difference between the first and last time in a circular manner
        min_diff = (1440 + minutes[0] - minutes[-1]) % 1440

        # Compare differences between adjacent times
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        return min_diff


if __name__ == "__main__":
    # Example test cases
    solution = Solution()

    # Test cases for both methods
    test_cases = [
        (["23:59", "00:00"], 1),      # Example 1
        (["00:00", "23:59", "00:00"], 0),  # Example 2, duplicate time
        (["01:00", "10:30", "03:15"], 135),  # Additional test case
        (["12:00", "23:59", "00:00"], 1),  # Circular edge case
    ]

    # Run test cases for both methods
    for i, (timePoints, expected) in enumerate(test_cases):
        result = solution.findMinDifference(timePoints.copy())
        assert result == expected, f"Test case {i + 1} failed for `findMinDifference`: {result} != {expected}"
        print(f"Test case {i + 1} passed for `findMinDifference`!")

        result_optimized = solution.findMinDifferenceOptimized(timePoints.copy())
        assert result_optimized == expected, f"Test case {i + 1} failed for `findMinDifferenceOptimized`: {result_optimized} != {expected}"
        print(f"Test case {i + 1} passed for `findMinDifferenceOptimized`!")

    print("All test cases passed!")
