from typing import List

class Solution:
    def smallestDistancePairBruteForce(self, nums: List[int], k: int) -> int:
        """
        Find the k-th smallest pair distance using a brute force approach.
        
        This method calculates the distance for all possible pairs in the array,
        sorts these distances, and then selects the k-th smallest one.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The k-th smallest distance to find.

        Returns:
            int: The k-th smallest distance.

        Time Complexity:
            O(n^2 log n): 
                - O(n^2) to generate all possible pairs.
                - O(n^2 log n) to sort the distances.

        Space Complexity:
            O(n^2): To store the list of distances.

        Intuition:
            - This method directly tackles the problem by generating all pairs
              and sorting their distances. It is easy to understand but inefficient
              for large inputs due to the large number of pairs (n choose 2).
        """
        n: int = len(nums)
        dist: List[int] = []
        
        # Create all pairs and calculate their distances
        for i in range(n-1):
            for j in range(i + 1, n):
                dist.append(abs(nums[i] - nums[j]))
        
        # Sort the distances
        dist.sort()
        
        # Return the k-th smallest distance
        return dist[k-1]

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        Find the k-th smallest pair distance using a binary search approach.

        This method uses binary search on the distance value to find the k-th 
        smallest distance. It combines sorting the input list with a helper function
        that counts the number of pairs with distances less than or equal to a given 
        value.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The k-th smallest distance to find.

        Returns:
            int: The k-th smallest distance.

        Time Complexity:
            O(n log d + n log n):
                - O(n log n) to sort the array.
                - O(n log d) for the binary search where `d` is the difference 
                  between the maximum and minimum elements in the array.
                - O(n) for the helper function that counts pairs within each 
                  binary search iteration.

        Space Complexity:
            O(1): No additional space proportional to the input size, apart from 
            variables used.

        Intuition:
            - Instead of generating and sorting all possible pair distances, we realize
              that we can perform binary search on the possible distances. We efficiently 
              count the number of pairs that have a distance less than or equal to the 
              mid-point in our search. This approach significantly reduces the time 
              complexity, making it feasible for large inputs.
        """
        nums.sort()
        l: int = 0
        r: int = nums[-1] - nums[0]  # Maximum possible distance

        def helper(dist: int) -> int:
            """
            Helper function to count the total number of pairs with distance <= dist.

            This function uses a two-pointer technique on the sorted array to count 
            how many pairs have a distance less than or equal to the given `dist`.

            Args:
                dist (int): The distance threshold.

            Returns:
                int: The number of pairs with distance <= dist.
            """
            l = 0
            res = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > dist:
                    l += 1
                res += r - l
            return res

        # Binary search to find the k-th smallest distance
        while l < r:
            m = l + (r - l) // 2
            pairs = helper(m)
            if pairs >= k:
                r = m  # Narrow down the search to the left
            else:
                l = m + 1  # Narrow down the search to the right

        return r

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 3, 1], 1, 0),
        ([1, 1, 1], 2, 0),
        ([1, 6, 1], 3, 5),
        ([1, 2, 3, 4], 5, 2),
        ([1, 3, 1, 2, 5, 4], 7, 2)
    ]

    # Run the test cases
    for i, (nums, k, expected) in enumerate(test_cases):
        if len(nums) <= 10**3:
            brute_force_result = solution.smallestDistancePairBruteForce(nums.copy(), k)
            assert brute_force_result == expected, f"Brute Force Test case {i+1} failed: expected {expected}, got {brute_force_result}"
        
        binary_search_result = solution.smallestDistancePair(nums.copy(), k)
        assert binary_search_result == expected, f"Binary Search Test case {i+1} failed: expected {expected}, got {binary_search_result}"

    print("All test cases passed!")