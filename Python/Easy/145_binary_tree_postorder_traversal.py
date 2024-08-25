"""
145. Binary Tree Postorder Traversal
Solved - Easy
Topics: Stack, Tree, Depth-First Search

Problem:
Given the root of a binary tree, return the postorder traversal of its nodes'
values.
The postorder traversal visits nodes in the order of left subtree, right
subtree, and then root.

Follow-up: The recursive solution is trivial; could you do it iteratively?

Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

from typing import List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    """Example class used by Leetcode"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversalTwoLists(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative postorder traversal using two lists: one for nodes and one
        for visited flags.
        This approach may translate better to other languages that don't
        support tuples as in Python.

        Time Complexity: O(N) - Each node is processed twice.
        Space Complexity: O(N) - Stack and visited list could grow to size N
        in the worst case.
        """
        if not root:
            return []

        stack: List[Optional[TreeNode]] = [root]
        visited: List[bool] = [False]
        res: List[int] = []

        while stack:
            cur = stack.pop()
            v = visited.pop()

            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True)
                    if cur.right:
                        stack.append(cur.right)
                        visited.append(False)
                    if cur.left:
                        stack.append(cur.left)
                        visited.append(False)

        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative postorder traversal using a single stack where each element
        is a tuple of the node and a visited flag.
        This approach optimizes space usage and is simpler to implement in
        Python.

        Time Complexity: O(N) - Each node is processed twice.
        Space Complexity: O(N) - Stack could grow to size N in the worst case.
        """
        if not root:
            return []

        stack: List[Tuple[TreeNode, bool]] = [(root, False)]
        res: List[int] = []

        while stack:
            cur, visited = stack.pop()

            if visited:
                res.append(cur.val)
            else:
                # Push root first so it's processed after left and right children
                stack.append((cur, True))
                if cur.right:
                    stack.append((cur.right, False))
                if cur.left:
                    stack.append((cur.left, False))

        return res


if __name__ == "__main__":
    # Test cases
    root1 = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    root2 = None
    root3 = TreeNode(1)

    # List of test cases
    test_cases = [
        (root1, [3, 2, 1]),
        (root2, []),
        (root3, [1]),
    ]

    solution = Solution()

    for i, (root, expected) in enumerate(test_cases):
        assert solution.postorderTraversalTwoLists(root) == expected, f"""
        Test case {i + 1} failed with TwoLists"""
        assert solution.postorderTraversal(root) == expected, f"""
        Test case {i + 1} failed with SingleStack"""

    print("All test cases passed!")
