"""
21. Merge Two Sorted Lists

Problem Statement: You are given the heads of two sorted linked lists `list1`
and `list2`. Merge the two lists into one sorted list. The list should be made
by splicing together the nodes of the first two lists. Return the head of the
merged linked list.

Example 1:
    Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
    Output: [1, 1, 2, 3, 4, 4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    - The number of nodes in both lists is in the range [0, 50].
    - -100 <= Node.val <= 100
    - Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    This class provides a solution to merge two sorted linked lists into one
    sorted linked list. The solution uses a dummy node to act as the starting
    point of the merged list and traverses both lists, choosing the smaller
    value at each step. The remaining nodes from either list1 or list2 are then
    attached to the merged list.
    """
    def mergeTwoLists(self,
                      list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted linked list.

        Time Complexity: O(n + m), where n and m are the lengths of list1 and
        list2 respectively. Space Complexity: O(1) as we are only using
        constant space apart from the input lists.

        Args:
            list1: Optional[ListNode] - The head of the first sorted linked
            list. list2: Optional[ListNode] - The head of the second sorted
            linked list.

        Returns:
            Optional[ListNode] - The head of the merged sorted linked list.
        """
        # Edge cases: one or both lists are empty
        if not list1:
            return list2
        if not list2:
            return list1

        # Dummy node to act as the starting point of the merged list
        dummy = ListNode()
        current = dummy

        p1, p2 = list1, list2  # Pointers for list1 and list2

        # Traverse both lists, choosing the smaller value at each step
        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        # Attach the remaining nodes from either list1 or list2
        if p1:
            current.next = p1
        else:
            current.next = p2

        # Return the merged list, skipping the dummy node
        return dummy.next


# Helper function to create linked list from list (for testing)
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to Python list (for testing)
def linked_list_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]

    solution = Solution()

    for i, (list1_vals, list2_vals, expected) in enumerate(test_cases):
        l1 = create_linked_list(list1_vals)
        l2 = create_linked_list(list2_vals)

        merged_head = solution.mergeTwoLists(l1, l2)
        result = linked_list_to_list(merged_head)

        assert result == expected, \
            f"Test case {i+1} failed: Expected {expected}, but got {result}"

    print("All test cases passed!")
