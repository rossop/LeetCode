from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Return all elements of the matrix in spiral order using the boundary method.

        This method uses four boundaries (left, right, top, bottom) to control the 
        traversal direction (right, down, left, up) and collects elements in spiral order.

        Args:
            matrix (List[List[int]]): The input m x n matrix.

        Returns:
            List[int]: A list containing all elements of the matrix in spiral order.

        Time Complexity:
            O(m * n): Where m is the number of rows and n is the number of columns 
            in the matrix. Each element is visited once.

        Space Complexity:
            O(1): Additional space is minimal (only the result list and a few variables 
            are used, excluding the space for the output list).
        """
        if not matrix or not matrix[0]:
            return []

        left_wall: int = 0
        right_wall: int = len(matrix[0]) - 1
        top_wall: int = 0
        bottom_wall: int = len(matrix) - 1

        sol: List[int] = []

        while left_wall <= right_wall and top_wall <= bottom_wall:
            # Traverse from left to right across the top wall
            for col in range(left_wall, right_wall + 1):
                sol.append(matrix[top_wall][col])
            top_wall += 1  # Move the top wall down

            # Traverse from top to bottom along the right wall
            for row in range(top_wall, bottom_wall + 1):
                sol.append(matrix[row][right_wall])
            right_wall -= 1  # Move the right wall left

            # Traverse from right to left across the bottom wall
            if top_wall <= bottom_wall:
                for col in range(right_wall, left_wall - 1, -1):
                    sol.append(matrix[bottom_wall][col])
                bottom_wall -= 1  # Move the bottom wall up

            # Traverse from bottom to top along the left wall
            if left_wall <= right_wall:
                for row in range(bottom_wall, top_wall - 1, -1):
                    sol.append(matrix[row][left_wall])
                left_wall += 1  # Move the left wall right

        return sol

    def spiralOrderWithMask(self, matrix: List[List[int]]) -> List[int]:
        """
        Return all elements of the matrix in spiral order using a direction array and visited mask.

        This method uses a direction array to manage the movement directions (right, down, 
        left, up) and a visited matrix to keep track of visited elements. The traversal 
        continues until all elements are visited.

        Args:
            matrix (List[List[int]]): The input m x n matrix.

        Returns:
            List[int]: A list containing all elements of the matrix in spiral order.

        Time Complexity:
            O(m * n): Where m is the number of rows and n is the number of columns 
            in the matrix. Each element is visited once.

        Space Complexity:
            O(m * n): Due to the additional space used by the visited mask.
        """
        if not matrix or not matrix[0]:
            return []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        current_direction = 0
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        sol = []

        r = c = 0
        for _ in range(m * n):
            sol.append(matrix[r][c])
            visited[r][c] = True
            nr, nc = r + directions[current_direction][0], c + directions[current_direction][1]

            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                r, c = nr, nc
            else:
                current_direction = (current_direction + 1) % 4
                r, c = r + directions[current_direction][0], c + directions[current_direction][1]

        return sol

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ([[1]], [1]),
        ([[1, 2], [3, 4]], [1, 2, 4, 3]),
        ([[1, 2, 3, 4]], [1, 2, 3, 4]),
        ([[1], [2], [3], [4]], [1, 2, 3, 4])
    ]

    for i, (matrix, expected) in enumerate(test_cases):
        result1 = solution.spiralOrder(matrix)
        result2 = solution.spiralOrderWithMask(matrix)
        assert result1 == expected, f"Test case {i+1} failed for spiralOrder: expected {expected}, got {result1}"
        assert result2 == expected, f"Test case {i+1} failed for spiralOrderWithMask: expected {expected}, got {result2}"

    print("All test cases passed!")