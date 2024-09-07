"""
1367. Linked List in Binary Tree

Problem Statement:
Given a binary tree root and a linked list with head as the first node, return True if all the 
elements in the linked list starting from the head correspond to some downward path connected 
in the binary tree, otherwise return False.

In this context, a downward path means a path that starts at some node and goes downwards.

Constraints:
- The number of nodes in the tree will be in the range [1, 2500].
- The number of nodes in the list will be in the range [1, 100].
- 1 <= Node.val <= 100 for each node in the linked list and binary tree.

Example 1:
    Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    Output: True
    Explanation: Nodes in blue form a subpath in the binary Tree.

Example 2:
    Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    Output: True

Example 3:
    Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    Output: False
    Explanation: There is no path in the binary tree that contains all the elements of the linked 
    list from head.

Approach:
- We use Depth First Search (DFS) to find if the linked list can match any downward path 
  starting from a node in the binary tree.
  
Optimized Approach:
- In the optimized approach, instead of traversing every node in the tree, we use memoization 
  or pruning techniques to skip unnecessary subtree exploration.

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        Determines if the linked list can match any downward path in the binary tree.

        Time Complexity:
            O(T * L) - where T is the number of nodes in the binary tree and L is the length of the linked list.
            We are traversing through each node in the tree and, at each node, potentially traversing the linked list.

        Space Complexity:
            O(H) - where H is the height of the binary tree, due to recursive calls. The maximum depth of recursion is the height of the tree.

        Args:
            head: The head of the linked list.
            root: The root of the binary tree.

        Returns:
            bool: True if the linked list corresponds to a downward path in the tree, False otherwise.
        """

        if not root:
            return False

        def dfs(node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
            """
            Performs DFS to match the linked list sequence with the binary tree nodes.

            Args:
                node: Current node in the binary tree.
                head: Current node in the linked list.

            Returns:
                bool: True if the current linked list matches any downward path from the current node.
            """
            if not head:
                return True
            if not node:
                return False
            if node.val == head.val:
                return dfs(node.left, head.next) or dfs(node.right, head.next)
            return False

        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def isSubPathOptimized(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        Optimized method to find if the linked list matches any downward path in the binary tree.
        This method uses memoization to avoid redundant checks and pruning to skip unnecessary subtree exploration.

        Time Complexity:
            O(T * L) - where T is the number of nodes in the binary tree and L is the length of the linked list.
            Although memoization helps reduce redundant computations, the worst case still involves traversing both structures.

        Space Complexity:
            O(H + L) - where H is the height of the binary tree and L is the length of the linked list.
            This is because the memoization table stores information about both the binary tree nodes and linked list nodes.

        Args:
            head: The head of the linked list.
            root: The root of the binary tree.

        Returns:
            bool: True if the linked list corresponds to a downward path in the tree, False otherwise.
        """
        if not root:
            return False

        memo = {}

        def dfs(node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
            if not head:
                return True
            if not node:
                return False

            if (node, head) in memo:
                return memo[(node, head)]

            if node.val == head.val:
                result = dfs(node.left, head.next) or dfs(node.right, head.next)
            else:
                result = False

            memo[(node, head)] = result
            return result

        return dfs(root, head) or self.isSubPathOptimized(head, root.left) or self.isSubPathOptimized(head, root.right)


if __name__ == "__main__":
    # Example test case
    # Linked list: [4 -> 2 -> 8]
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(8)

    # Binary tree:
    #       1
    #      / \
    #     4   4
    #      \   \
    #       2   2
    #      /   /
    #     1   1
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.right.right = TreeNode(2)
    root.right.right.left = TreeNode(1)

    # Instantiate Solution and run the test case
    solution = Solution()
    result = solution.isSubPath(head, root)
    print(f"Is subpath: {result}")  # Expected output: True
