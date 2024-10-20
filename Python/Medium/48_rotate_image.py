from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the matrix 90 degrees clockwise in-place.
        
        The function first transposes the matrix (by swapping matrix[i][j] with matrix[j][i]),
        and then reverses each row to achieve the 90-degree rotation.

        Time Complexity:
            O(n^2): The algorithm iterates over the matrix twice, first to transpose it and 
            then to reverse each row. Both operations have a time complexity of O(n^2).

        Space Complexity:
            O(1): The matrix is modified in-place, so no additional space proportional to the 
            input size is used.
        
        Args:
            matrix (List[List[int]]): A 2D list representing the matrix to be rotated.
        
        Returns:
            None: The matrix is modified in-place.
        """
        n: int = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):  # Note: j starts from i + 1 to avoid redundant swaps
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()