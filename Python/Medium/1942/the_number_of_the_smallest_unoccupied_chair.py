import heapq
from typing import List, Tuple

class Solution:
    """
    This class provides two methods to solve the problem of determining which chair the target friend will sit on.
    It uses heaps (min-heaps) to efficiently manage the smallest available chair and keep track of when chairs are vacated.
    """

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        """
        Determines the smallest chair number that the targetFriend will sit on.
        
        This version uses a list of indexes to keep track of friends sorted by their arrival times and manages chair
        assignments with min-heaps.
        
        Args:
            times (List[List[int]]): A 2D list where each sublist represents the arrival and leaving times of a friend.
            targetFriend (int): The index of the target friend in the original `times` list.
        
        Returns:
            int: The chair number that the target friend will sit on.
        """
        # List of indexes to keep track of friends, sorted by arrival times
        indexes: List[int] = [i for i in range(len(times))]
        indexes.sort(key=lambda i : times[i][0])

        # Min-heap to track used chairs with their leaving times
        used_chairs: List[Tuple[int, int]] = []  # (leaving_time, chair)
        
        # Min-heap to track available chairs
        available_chairs: List[int] = [i for i in range(len(times))]  # Initially, all chairs are available

        for i in indexes:
            a, l = times[i]  # Arrival and leaving time of the i-th friend

            # Free up chairs for any friends who have left by this arrival time
            while used_chairs and used_chairs[0][0] <= a:
                leave, chair = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, chair)
            
            # Assign the smallest available chair to the current friend
            chair = heapq.heappop(available_chairs)
            heapq.heappush(used_chairs, (l, chair))

            # If this friend is the targetFriend, return the chair number
            if i == targetFriend:
                return chair

    def smallestChairTuple(self, times: List[List[int]], targetFriend: int) -> int:
        """
        Determines the smallest chair number that the targetFriend will sit on.
        
        This version stores the arrival, leaving, and index of friends as a tuple, and manages chair assignments with min-heaps.
        
        Args:
            times (List[List[int]]): A 2D list where each sublist represents the arrival and leaving times of a friend.
            targetFriend (int): The index of the target friend in the original `times` list.
        
        Returns:
            int: The chair number that the target friend will sit on.
        """
        # List of tuples (arrival_time, leaving_time, friend_index)
        times: List[Tuple[int, int, int]] = [(t[0], t[1], i) for i, t in enumerate(times)]
        times.sort()  # Sort by arrival times

        # Min-heap to track used chairs with their leaving times
        used_chairs: List[Tuple[int, int]] = []  # (leaving_time, chair)

        # Min-heap to track available chairs
        available_chairs: List[int] = [i for i in range(len(times))]  # Initially, all chairs are available

        for a, l, i in times:
            # Free up chairs for any friends who have left by this arrival time
            while used_chairs and used_chairs[0][0] <= a:
                leave, chair = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, chair)
            
            # Assign the smallest available chair to the current friend
            chair = heapq.heappop(available_chairs)
            heapq.heappush(used_chairs, (l, chair))

            # If this friend is the targetFriend, return the chair number
            if i == targetFriend:
                return chair
