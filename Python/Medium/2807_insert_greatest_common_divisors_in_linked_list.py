"""
2807. Insert Greatest Common Divisors in Linked List

Problem Statement:
Given the head of a linked list where each node contains an integer value, insert 
a new node between every pair of adjacent nodes. The value of the new node should 
be equal to the greatest common divisor (GCD) of the two adjacent nodes' values. 

Return the modified linked list after inserting these nodes.

Constraints:
- The number of nodes in the list is in the range [1, 5000].
- 1 <= Node.val <= 1000

Example 1:
    Input: head = [18, 6, 10, 3] 
    Output: [18, 6, 6, 2, 10, 1, 3]

Example 2:
    Input: head = [7]
    Output: [7]

Approach:
- Traverse the linked list while maintaining pointers to two adjacent nodes.
- For each pair of adjacent nodes, compute the greatest common divisor (GCD) and 
  insert a new node with this value between the two nodes.
- Continue until reaching the end of the list.
"""

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    A class that provides methods to insert the greatest common divisor (GCD)
    between each pair of adjacent nodes in a linked list.
    """

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Inserts nodes with the greatest common divisor (GCD) between each pair of adjacent nodes.

        Time Complexity:
            O(n * log(min(a, b))) - For each node, we compute the GCD of two adjacent nodes. 
            The GCD operation using the Euclidean algorithm takes O(log(min(a, b))), where a and b 
            are the values of the adjacent nodes. Since we process all n nodes in the list, the 
            overall complexity is O(n * log(min(a, b))).

        Space Complexity:
            O(1) - We are modifying the linked list in-place and only using a few variables for 
            traversal and GCD computation.

        Args:
            head: The head of the linked list.

        Returns:
            The modified linked list after inserting GCD nodes.
        """
        if head.next is None:
            return head

        def gcd(a: int, b: int) -> int:
            """Calculates the greatest common divisor (GCD) of two integers."""
            while b != 0:
                a, b = b, a % b
            return a

        n1: ListNode = head
        while n1.next is not None:
            n2 = n1.next
            # Compute GCD of adjacent nodes
            gcd_value = gcd(n1.val, n2.val)
            # Insert a new node with the GCD value between n1 and n2
            gcd_node = ListNode(val=gcd_value, next=n2)
            n1.next = gcd_node
            # Move n1 to n2 (the original next node)
            n1 = n2
        
        return head

    def insertGreatestCommonDivisorsOptimized(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Optimized solution to insert nodes with the greatest common divisor (GCD) between each pair 
        of adjacent nodes using recursion for GCD.

        Time Complexity:
            O(n * log(min(a, b))) - For each node, we compute the GCD of two adjacent nodes. 
            The GCD operation using the recursive Euclidean algorithm takes O(log(min(a, b))). 
            Since we process all n nodes in the list, the overall complexity remains the same.

        Space Complexity:
            O(1) - In-place modification of the linked list without additional space.

        Args:
            head: The head of the linked list.

        Returns:
            The modified linked list after inserting GCD nodes.
        """
        if not head or not head.next:
            return head

        def gcd_recursive(a: int, b: int) -> int:
            """Recursive Euclidean algorithm for computing the greatest common divisor (GCD)."""
            if b == 0:
                return a
            return gcd_recursive(b, a % b)

        n1: ListNode = head
        while n1 and n1.next:
            n2 = n1.next
            gcd_value = gcd_recursive(n1.val, n2.val)
            # Insert GCD node
            n1.next = ListNode(val=gcd_value, next=n2)
            n1 = n2  # Move to the next original node

        return head


# Helper function to convert a list to a linked list
def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list back to a list for easy comparison
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([18, 6, 10, 3], [18, 6, 6, 2, 10, 1, 3]),  # Example 1
        ([7], [7]),                                  # Example 2
        ([12, 15, 18], [12, 3, 15, 3, 18]),          # Custom Test Case 1
        ([100, 50], [100, 50, 50]),                  # Custom Test Case 2
    ]
    
    # Instantiate the solution class
    solution = Solution()

    # Loop through test cases
    for i, (input_list, expected_output) in enumerate(test_cases):
        # Create linked list from input list
        head = create_linked_list(input_list)
        # Test with the first method
        modified_head = solution.insertGreatestCommonDivisors(head)
        assert linked_list_to_list(modified_head) == expected_output, \
            f"Test case {i+1} failed for original method"

        # Create linked list again for the optimized method
        head = create_linked_list(input_list)
        # Test with the optimized method
        modified_head_optimized = solution.insertGreatestCommonDivisorsOptimized(head)
        assert linked_list_to_list(modified_head_optimized) == expected_output, \
            f"Test case {i+1} failed for optimized method"
    
    print("All test cases passed!")
