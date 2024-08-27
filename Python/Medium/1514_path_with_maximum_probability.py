"""
Problem: Given an undirected weighted graph of `n` nodes (0-indexed), where
edges[i] = [a, b] represents an undirected edge connecting the nodes a and b
with a probability of success of traversing that edge succProb[i].

Given two nodes `start` and `end`, find the path with the maximum probability
of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted
if it differs from the correct answer by at most 1e-5.

Link to the problem:
https://leetcode.com/problems/path-with-maximum-probability/
"""
import heapq
import collections
from typing import List, Dict


class Solution:
    """
    A class that provides multiple solutions to the "Path with Maximum
    Probability" problem.
    """

    def maxProbability(self, n: int, edges: List[List[int]],
                       succProb: List[float], start_node: int,
                       end_node: int) -> float:
        """
        Implements Dijkstra's algorithm using a max-heap (priority queue) to
        find the maximum probability path.

        Instead of minimizing distances, this algorithm maximizes the
        probabilities by multiplying them. The graph is represented as an
        adjacency list.

        Args:
            n (int): The number of nodes in the graph.
            edges (List[List[int]]): List of edges, each represented as [u, v].
            succProb (List[float]): List of success probabilities corresponding
                                    to each edge.
            start_node (int): The start node.
            end_node (int): The end node.

        Returns:
            float: The max probability to reach `end_node` from `start_node`.
        """
        
        adj: Dict[int, List[List[int]]] = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        pq: List[List[float]] = [(-1, start_node)]
        visit: set = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            prob *= -1  # Convert back to positive probability

            if cur == end_node:
                return prob

            visit.add(cur)

            for neighbor, edgeProb in adj[cur]:
                if neighbor not in visit:
                    heapq.heappush(pq, (-(prob * edgeProb), neighbor))

        return 0.0

    def maxProbabilityBFS(self, n: int, edges: List[List[int]],
                          succProb: List[float], start_node: int,
                          end_node: int) -> float:
        """
        An alternative solution using Breadth-First Search (BFS) with a queue
        to find the maximum probability path.

        Instead of using a priority queue, it uses a regular queue and tracks
        the highest probability seen for each node.

        Args:
            n (int): The number of nodes in the graph. edges (List[List[int]]):
            List of edges, each represented as [u, v]. succProb (List[float]):
            List of success probabilities corresponding to each edge.
            start_node (int): The start node. end_node (int): The end node.

        Returns:
            float: The maximum probability to reach `end_node` from
            `start_node`.
        """

        adj: Dict[int, List[List[int]]] = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        queue = collections.deque([(1, start_node)])
        probabilities: Dict[int, float] = {start_node: 1}

        while queue:
            prob, cur = queue.popleft()

            if cur == end_node:
                return prob

            for neighbor, edgeProb in adj[cur]:
                new_prob = prob * edgeProb
                if new_prob > probabilities.get(neighbor, 0):
                    probabilities[neighbor] = new_prob
                    queue.append((new_prob, neighbor))

        return 0.0

if __name__ == "__main__":
    # Example Test Cases
    test_cases = [
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2, 0.25),
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2, 0.3),
        (3, [[0, 1]], [0.5], 0, 2, 0.0)
    ]

    solution = Solution()
    for i, (n, edges, succProb, start_node, end_node, expected) in enumerate(test_cases):
        assert solution.maxProbability(n, edges, succProb, start_node, end_node) == expected, \
            f"Test case {i + 1} failed."
        assert solution.maxProbabilityBFS(n, edges, succProb, start_node, end_node) == expected, \
            f"Test case {i + 1} failed (BFS)."

    print("All test cases passed!")
