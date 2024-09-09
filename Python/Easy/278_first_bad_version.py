"""
278. First Bad Version
Link: https://leetcode.com/problems/first-bad-version/

This file contains a solution to the "First Bad Version" problem. The solution is implemented 
in the `Solution` class, which provides methods to find the first bad version of a product 
given a range of versions [1, 2, ..., n]. The problem is solved using a binary search approach 
to minimize the number of API calls, as well as a brute-force method for comparison.
"""

class Solution:
    """
    Solution class for the "First Bad Version" problem.

    You are a product manager and currently leading a team to develop a new product. 
    Unfortunately, the latest version of your product fails the quality check. Since each 
    version is developed based on the previous version, all the versions after a bad version 
    are also bad.

    The `Solution` class provides two methods:
    1. `firstBadVersion`: Implements a binary search to efficiently find the first bad version.
    2. `firstBadVersionBruteForce`: Implements a brute-force approach by checking each version sequentially.

    Additionally, the class provides:
    - `isBadVersion`: A method to simulate the API that checks if a version is bad.
    - `badVersion`: A property with a setter to specify the bad version for testing purposes.
    """
    def __init__(self):
        self._bad_version = None

    @property
    def badVersion(self) -> int:
        """
        Property to get the current bad version.

        Returns:
            int: The version number that is considered the first bad version.
        """
        return self._bad_version

    @badVersion.setter
    def badVersion(self, version: int) -> None:
        """
        Setter to define the bad version.

        Args:
            version (int): The version number that is the first bad version.
        """
        self._bad_version = version

    def isBadVersion(self, version: int) -> bool:
        """
        Determines if a given version is bad.

        Args:
            version (int): The version number to check.

        Returns:
            bool: True if the version is bad, False otherwise.
        """
        return version >= self._bad_version

    def firstBadVersion(self, n: int) -> int:
        """
        Finds the first bad version using a binary search to minimize the number of API calls.

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Args:
            n (int): The total number of versions.

        Returns:
            int: The version number of the first bad version.
        """
        L: int = 1
        R: int = n
        
        while L < R:
            M: int = (L + R) // 2
            if self.isBadVersion(M):
                R = M  # If M is bad, search the left half including M
            else:
                L = M + 1  # If M is good, search the right half excluding M

        return L

    def firstBadVersionBruteForce(self, n: int) -> int:
        """
        Finds the first bad version using a brute-force approach by checking each version sequentially.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            n (int): The total number of versions.

        Returns:
            int: The version number of the first bad version.
        """
        for i in range(1, n + 1):
            if self.isBadVersion(i):
                return i
        return -1  # Should never reach here as there's always a bad version in the input


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (5, 4),  # Example 1: (n, bad_version)
        (1, 1),  # Example 2: (n, bad_version)
        (10, 3), # Additional case
        (10, 10) # Additional case
    ]

    for i, (n, bad_version) in enumerate(test_cases, 1):
        solution.badVersion = bad_version
        assert solution.firstBadVersion(n) == bad_version, f"Test case {i} failed for firstBadVersion"
        assert solution.firstBadVersionBruteForce(n) == bad_version, f"Test case {i} failed for firstBadVersionBruteForce"

    print("All test cases passed!")