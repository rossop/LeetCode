"""
590. N-ary Tree Postorder Traversal
Solved - Easy
Topics: Stack, Tree, Depth-First Search

Problem:
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

N-ary Tree input serialization is represented in their level order traversal. Each group of children is separated by a null value.

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
- The height of the n-ary tree is less than or equal to 1000.

Follow-up:
Recursive solution is trivial, could you do it iteratively?

Link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""

from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        Iterative postorder traversal of an N-ary tree using a stack and a visited list.
        This method uses two stacks to simulate the postorder traversal iteratively.

        Time Complexity: O(N) - Each node is visited exactly once.
        Space Complexity: O(N) - Stack and visited list could grow to size N in the worst case.

        Args:
            root (Node): The root node of the N-ary tree.

        Returns:
            List[int]: A list of node values in postorder traversal.
        """
        if not root:
            return []

        stack: List[Node] = [root]
        visited: List[bool] = [False]

        res: List[int] = []

        while stack:
            cur, v = stack.pop(), visited.pop()

            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True)
                    for child in reversed(cur.children):
                        stack.append(child)
                        visited.append(False)

        return res

    def postorderSingleStack(self, root: 'Node') -> List[int]:
        """
        Optimized iterative postorder traversal of an N-ary tree using a single stack.
        This method uses a single stack and reverses the result at the end to achieve postorder.

        Time Complexity: O(N) - Each node is visited exactly once.
        Space Complexity: O(N) - Stack could grow to size N in the worst case.

        Args:
            root (Node): The root node of the N-ary tree.

        Returns:
            List[int]: A list of node values in postorder traversal.
        """
        if not root:
            return []

        stack: List[Node] = [root]
        res: List[int] = []

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children)  # Push all children to stack
            
        return res[::-1]  # Reverse the result to get the correct postorder

    def postorderRecursive(self, root: 'Node') -> List[int]:
        """
        Recursive postorder traversal of an N-ary tree.

        Time Complexity: O(N) - Each node is visited exactly once.
        Space Complexity: O(N) - Recursion stack could grow to size N in the worst case.

        Args:
            root (Node): The root node of the N-ary tree.

        Returns:
            List[int]: A list of node values in postorder traversal.
        """
        res: List[int] = []
        def traverse(node: 'Node'):
            if node:
                for child in node.children:
                    traverse(child)
                res.append(node.val)
        
        traverse(root)
        return res

if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Test case 1
        {
            "tree": [1, None, 3, 2, 4, None, 5, 6],
            "expected": [5, 6, 3, 2, 4, 1]
        },
        # Test case 2
        {
            "tree": [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14],
            "expected": [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
        },
        # Additional Test case 3: Single node tree
        {
            "tree": [1],
            "expected": [1]
        },
        # Additional Test case 4: Empty tree
        {
            "tree": [],
            "expected": []
        },
        # Additional Test case 5: Tree with one level of children
        {
            "tree": [1, None, 2, 3, 4, 5],
            "expected": [2, 3, 4, 5, 1]
        }
    ]
    
    def create_tree(data: List[Optional[int]]) -> Optional[Node]:
        """ GPT generated
        """
        if not data:
            return None
        root = Node(data[0])
        queue = [root]
        i = 1
        while i < len(data):
            parent = queue.pop(0)
            while i < len(data) and data[i] is not None:
                child = Node(data[i])
                parent.children.append(child)
                queue.append(child)
                i += 1
            i += 1  # Skip the None
        return root

    solution = Solution()
    for i, test in enumerate(test_cases):
        root = create_tree(test["tree"])
        assert solution.postorder(root) == test["expected"], f"Test case {i + 1} failed"
        assert solution.postorderSingleStack(root) == test["expected"], f"Test case {i + 1} (Single Stack) failed"
        assert solution.postorderRecursive(root) == test["expected"], f"Test case {i + 1} (Recursive) failed"

    print("All test cases passed!")
