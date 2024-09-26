"""
729. My Calendar I

Problem Statement:
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end),
the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:
- MyCalendar() Initializes the calendar object.
- book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking.
Otherwise, return false and do not add the event to the calendar.

Example 1:
Input:
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output:
[null, true, false, true]

Explanation:
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, double booking with [10, 20].
myCalendar.book(20, 30); // return True, no overlap.

Constraints:
- 0 <= start < end <= 10^9
- At most 1000 calls will be made to book.
"""

from typing import List, Tuple

class MyCalendar:
    """
    This class implements a calendar where events can be booked without
    overlapping.

    Methods: 1. book: A simple implementation that checks all existing events
    for overlaps. 2. book2: A memory-intensive variant that stores every booked
    time individually.

    - book is more efficient for larger inputs, especially when working with
      large ranges.
    - book2 can be inefficient as it checks each individual time between start
      and end.
    """

    def __init__(self):
        """Initializes the calendar object."""
        self.calendar: List[Tuple[int, int]] = []
        self.times = set()

    def book(self, start: int, end: int) -> bool:
        """
        Checks whether the given event can be added to the calendar without
        overlap. If there is no overlap, it adds the event and returns True,
        otherwise False.

        Time Complexity: O(n), where n is the number of booked events. Space
        Complexity: O(n), for storing booked events.

        Args:
            start: int - Start time of the event. end: int - End time of the
            event.

        Returns:
            bool - True if the event can be booked, False if it causes an
            overlap.
        """
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True

    def book2(self, start: int, end: int) -> bool:
        """
        A less memory-efficient implementation that checks and stores each
        individual time between start and end.

        Time Complexity: O(end - start), as it checks each time in the given
            range.
        Space Complexity: O(total booked times), which can be very large.

        Args:
            start: int - Start time of the event. end: int - End time of the
            event.

        Returns:
            bool - True if the event can be booked, False if it causes an
            overlap.
        """
        for time in range(start, end):
            if time in self.times:
                return False

        for time in range(start, end):
            self.times.add(time)

        return True


# Test cases to validate the solution
if __name__ == "__main__":
    myCalendar = MyCalendar()

    # Using the book method
    print("Testing book method:")
    assert myCalendar.book(10, 20) is True, "Test case 1 failed"
    assert myCalendar.book(15, 25) is False, "Test case 2 failed"
    assert myCalendar.book(20, 30) is True, "Test case 3 failed"
    print("All test cases passed for book method!")

    # Using the book2 method (will reset the MyCalendar object)
    print("\nTesting book2 method:")
    myCalendar2 = MyCalendar()
    assert myCalendar2.book2(10, 20) is True, "Test case 1 failed (book2)"
    assert myCalendar2.book2(15, 25) is False, "Test case 2 failed (book2)"
    assert myCalendar2.book2(20, 30) is True, "Test case 3 failed (book2)"
    print("All test cases passed for book2 method!")
