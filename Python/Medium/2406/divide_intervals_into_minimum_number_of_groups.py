from typing import List


class Solution:
    """
    This class provides three methods to solve the problem of dividing intervals into the minimum number of non-overlapping groups.
    
    Methods:
    1. minGroups: Uses a two-pointer technique similar to the Meeting Rooms II problem.
    2. minGroupsCount: A variant of the two-pointer technique, directly counting the number of overlapping intervals at each point.
    3. minGroupsGreedy: A brute-force approach that checks each point in the interval range.
    """

    def minGroups(self, intervals: List[List[int]]) -> int:
        """
        Solves the problem using the two-pointer approach by sorting the start and end times of the intervals.
        
        Time Complexity: O(n log n), where n is the number of intervals due to sorting.
        Space Complexity: O(n), where n is the number of intervals to store the start and end times.
        
        Args:
            intervals: A list of intervals where each interval is represented by a list of two integers [start, end].
        
        Returns:
            int: The minimum number of groups required such that no two intervals in the same group intersect.
        """
        start: List[int] = []
        end: List[int] = []

        # Split intervals into start and end times
        for l, r in intervals:
            start.append(l)
            end.append(r)

        # Sort the start and end times
        start.sort()
        end.sort()

        # Pointers for traversing start and end arrays
        i: int = 0
        j: int = 0

        res: int = 0  # To store the result

        while i < len(intervals):
            # If there is an overlap, we need a new group
            if start[i] <= end[j]:
                i += 1
            else:
                # If no overlap, the previous group can close
                j += 1
            # Calculate the number of overlapping intervals
            res = max(res, i - j)

        return res

    def minGroupsCount(self, intervals: List[List[int]]) -> int:
        """
        Uses the two-pointer technique and explicitly counts the number of groups at each step.
        
        Time Complexity: O(n log n), where n is the number of intervals due to sorting.
        Space Complexity: O(n), where n is the number of intervals to store the start and end times.
        
        Args:
            intervals: A list of intervals where each interval is represented by a list of two integers [start, end].
        
        Returns:
            int: The minimum number of groups required.
        """
        start: List[int] = []
        end: List[int] = []

        # Split intervals into start and end times
        for l, r in intervals:
            start.append(l)
            end.append(r)

        # Sort the start and end times
        start.sort()
        end.sort()

        i: int = 0
        j: int = 0

        res: int = 0  # To store the result
        groups: int = 0  # To track current number of overlapping intervals

        while i < len(intervals):
            # If there is an overlap, we increment the group count
            if start[i] <= end[j]:
                groups += 1
                i += 1
            else:
                # Otherwise, we decrement the group count as one interval ends
                groups -= 1
                j += 1
            res = max(res, groups)

        return res

    def minGroupsGreedy(self, intervals: List[List[int]]) -> int:
        """
        A brute-force greedy solution that checks every point in the interval range to determine the maximum number of overlapping intervals.
        
        Time Complexity: O((maxx - minn) * n), where maxx and minn are the maximum and minimum points in the interval range, and n is the number of intervals.
        Space Complexity: O(1) apart from input storage.
        
        Args:
            intervals: A list of intervals where each interval is represented by a list of two integers [start, end].
        
        Returns:
            int: The minimum number of groups required.
        """
        count: int = 0

        # Determine the smallest and largest points in the intervals
        minn: int = min(x for x, y in intervals)
        maxx: int = max(y for x, y in intervals)

        # Loop through each point in the range and count the number of overlapping intervals
        for i in range(minn, maxx + 1):
            val: int = 0
            for left, right in intervals:
                if left <= i <= right:
                    val += 1

            count = max(count, val)

        return count
