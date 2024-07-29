from typing import List

class Solution:
    """
    A class to solve the 'Merge Intervals' problem.

    Problem:
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
        and return an array of the non-overlapping intervals that cover all the intervals in the input.

        Example 1:
            Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
            Output: [[1,6],[8,10],[15,18]]
            Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

        Example 2:
            Input: intervals = [[1,4],[4,5]]
            Output: [[1,5]]
            Explanation: Intervals [1,4] and [4,5] are considered overlapping.

    Constraints:
        - 1 <= intervals.length <= 10^4
        - intervals[i].length == 2
        - 0 <= starti <= endi <= 10^4
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges overlapping intervals in the given list.

        The method first sorts the intervals based on their start times. It then iterates through the sorted
        intervals, merging overlapping intervals into one. Non-overlapping intervals are added to the result list as they are.

        Args:
            intervals (List[List[int]]): A list of intervals where each interval is a list of two integers [start, end].

        Returns:
            List[List[int]]: A list of merged intervals, with no overlapping intervals.

        Time Complexity:
            O(N log N) due to sorting the intervals, where N is the number of intervals.
            O(N) for the merge process, which iterates through the intervals once.

        Space Complexity:
            O(N) for storing the result list.

        """
        # Sort the intervals based on the start time
        intervals.sort(key=lambda interval: interval[0])

        # Initialize the list for merged intervals
        merged = []
        
        # Start by adding the first interval
        merged.append(intervals[0])

        # Iterate over the sorted intervals
        for start, stop in intervals[1:]:
            last_start, last_stop = merged[-1]

            # If the current interval does not overlap with the last one in merged, add it
            if start > last_stop:
                merged.append([start, stop])
            else:
                # If they overlap, merge the intervals by updating the stop time
                merged[-1] = [last_start, max(stop, last_stop)]

        return merged


if __name__ == "__main__":
    # Test cases with expected outcomes
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,4],[0,4]], [[0,4]]),
        ([[1,4],[2,3]], [[1,4]]),
        ([[1,4],[0,1]], [[0,4]])
    ]

    # Initialize the Solution class
    solution = Solution()

    # Run the test cases
    for i, (intervals, expected) in enumerate(test_cases, 1):
        assert solution.merge(intervals) == expected, f"Test case {i} failed"

    print("All test cases passed!")