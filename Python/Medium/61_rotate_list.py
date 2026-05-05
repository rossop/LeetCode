"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Constraints:
- The number of nodes in the list is in the range [0, 500].
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 10^9

Examples:

Example 1:
    Input: head = [1, 2, 3, 4, 5], k = 2
    Output: [4, 5, 1, 2, 3]

Example 2:
    Input: head = [0, 1, 2], k = 4
    Output: [2, 0, 1]
"""

from typing import Any, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode | Any, k: int) -> ListNode | Any:
        """
        Rotates the linked list to the right by k positions.

        Walks the list once to measure its length and capture the tail, then
        reduces k modulo the length so we never rotate further than needed.
        The new tail sits at index (length - 1 - k); splitting the list
        there and stitching the original tail to the original head completes
        the rotation in a single extra traversal.

        Time complexity:  O(n) — one pass to measure, one pass to pivot.
        Space complexity: O(1) — pointer rewiring only.
        """
        if not head:
            return head

        # Walk to the tail while counting nodes.
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        # Effective rotations after wrap-around.
        k = k % length
        if k == 0:
            return head

        # Advance to the node just before the new head.
        cur: ListNode | Any = head
        for _ in range(length - 1 - k):
            cur = cur.next

        new_head: ListNode | Any = cur.next
        cur.next = None
        tail.next = head

        return new_head


def create_linked_list(arr: list[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(node: Optional[ListNode]) -> list[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
        ([], 0, []),
        ([1], 99, [1]),
        ([1, 2], 3, [2, 1]),
    ]

    solution = Solution()

    for i, (vals, k, expected) in enumerate(test_cases, 1):
        head = create_linked_list(vals)
        rotated = solution.rotateRight(head, k)
        result = linked_list_to_list(rotated)
        assert result == expected, \
            f"Test case {i} failed: Expected {expected}, but got {result}"

    print("All test cases passed!")
