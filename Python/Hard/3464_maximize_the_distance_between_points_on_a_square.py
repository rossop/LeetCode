"""
3464. Maximize the Distance Between Points on a Square

You are given an integer side, representing the edge length of a square with
corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.

You are also given a positive integer k and a 2D integer array points, where
points[i] = [xi, yi] represents the coordinate of a point lying on the boundary
of the square.

You need to select k elements among points such that the minimum Manhattan
distance between any two points is maximized.

Return the maximum possible minimum Manhattan distance between the selected k
points.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is
|xi - xj| + |yi - yj|.

Constraints:
- 1 <= side <= 10^9
- 4 <= points.length <= min(4 * side, 15 * 10^3)
- points[i] == [xi, yi]
- points[i] lies on the boundary of the square
- All points[i] are unique
- 4 <= k <= min(25, points.length)

Examples:

Example 1:
    Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4
    Output: 2

Example 2:
    Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4
    Output: 1

Example 3:
    Input: side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5
    Output: 1
"""

from bisect import bisect_left


class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        """
        Binary search on the answer + greedy feasibility check via 1D perimeter
        coordinates.

        Perimeter mapping (counterclockwise from bottom-left):
          left edge  (x=0):     p = y
          top edge   (y=side):  p = side + x
          right edge (x=side):  p = 3*side - y
          bottom edge(y=0):     p = 4*side - x

        Key property: for k >= 4 the maximum achievable min-distance is <= side,
        so consecutive selected points (in perimeter order) span at most one
        corner. For same-side or adjacent-side pairs the perimeter arc distance
        equals the Manhattan distance, making the perimeter-based check exact.

        Feasibility check for a candidate minimum n:
          1. Greedily place k points starting from the smallest coordinate,
             using bisect_left to find the next coordinate >= curr + n.
          2. If the circular gap from the last point back to the first is also
             >= n (i.e. curr - res[0] <= 4*side - n), return True immediately.
          3. Otherwise slide the starting index from 1 up to idx[1]-1 and
             re-greedily advance the remaining k-1 pointers.

        Time complexity:  O(n log n + n*k*log(side))
        Space complexity: O(n)
        """
        res: list[int] = []
        for x, y in points:
            if x == 0:
                res.append(y)
            elif y == side:
                res.append(side + x)
            elif x == side:
                res.append(side * 3 - y)
            else:
                res.append(side * 4 - x)

        res.sort()

        def check(n: int) -> bool:
            idx: list[int] = [0] * k
            curr = res[0]
            for i in range(1, k):
                j = bisect_left(res, curr + n)
                if j == len(res):
                    return False
                idx[i] = j
                curr = res[j]
            if curr - res[0] <= side * 4 - n:
                return True

            for idx[0] in range(1, idx[1]):
                for j in range(1, k):
                    while res[idx[j]] < res[idx[j - 1]] + n:
                        idx[j] += 1
                        if idx[j] == len(res):
                            return False
                if res[idx[-1]] - res[idx[0]] <= side * 4 - n:
                    return True
            return False

        left, right = 1, side + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (2, [[0, 2], [2, 0], [2, 2], [0, 0]], 4, 2),
        (2, [[0, 0], [1, 2], [2, 0], [2, 2], [2, 1]], 4, 1),
        (2, [[0, 0], [0, 1], [0, 2], [1, 2], [2, 0], [2, 2], [2, 1]], 5, 1),
    ]

    for side, points, k, expected in test_cases:
        result = solution.maxDistance(side, points, k)
        assert result == expected, \
            f"maxDistance failed: side={side}, k={k} → expected {expected}, got {result}"
    print("All test cases passed!")
