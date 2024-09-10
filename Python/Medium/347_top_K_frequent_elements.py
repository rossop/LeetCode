"""
347. Top K Elements in List

Problem Statement: Given an integer array `nums` and an integer `k`, return the
`k` most frequent elements in the array. The test cases are generated such that
the answer is always unique.

You may return the output in any order.

Constraints: - 1 <= nums.length <= 10^4 - -1000 <= nums[i] <= 1000 - 1 <= k <=
number of distinct elements in nums

Example 1:
    Input: nums = [1, 2, 2, 3, 3, 3], k = 2 Output: [2, 3]

Example 2:
    Input: nums = [7, 7], k = 1 Output: [7]

Approach:
1. We will use a combination of bucket sort and hash map to efficiently get the
    top k frequent elements.
2. The hash map will track the frequency of each element, and then we will use
    bucket sort to store the numbers by their frequencies.
"""

from typing import List, Dict
from collections import Counter


class Solution:
    """
    A solution class that contains multiple methods to solve the 'Top K
    Frequent Elements' problem using different approaches.
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Solves the problem using bucket sort.

        Time Complexity:
            O(n), where n is the number of elements in `nums`. This is because
            we traverse the array once to build the frequency map and then
            use the bucket sort method to sort the elements.

        Space Complexity:
            O(n), where n is the number of elements in `nums`. We use a hash
            map for frequency count and a bucket array to store elements based
            on frequency.

        Args:
            nums: A list of integers.
            k: An integer representing the number of most frequent elements
               to return.

        Returns:
            A list of `k` most frequent elements from the array `nums`.
        """
        # Frequency count using hash map
        count: Dict[int, int] = Counter(nums)
        # Bucket sort: freq[i] stores the elements that appear i times
        freq: List[List[int]] = [[] for i in range(len(nums) + 1)]

        # Populate the bucket
        for n, c in count.items():
            freq[c].append(n)

        res: List[int] = []
        # Iterate through the bucket from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        """
        Solves the problem using a heap.

        Time Complexity:
            O(n log k), where n is the number of elements in `nums`. This is 
            because building the frequency map takes O(n), and pushing elements 
            into the heap takes O(log k).
        
        Space Complexity:
            O(n), where n is the number of elements in `nums`. The frequency 
            map requires O(n) space, and the heap uses O(k) space.

        Args:
            nums: A list of integers.
            k: An integer representing the number of most frequent elements 
               to return.

        Returns:
            A list of `k` most frequent elements from the array `nums`.
        """
        from heapq import nlargest
        count: Dict[int, int] = Counter(nums)
        # Extract the k largest elements from the frequency map
        return nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 2, 3, 3, 3], 2, [2, 3]),
        ([7, 7], 1, [7]),
        ([4, 4, 4, 4, 5, 5, 5, 6, 6], 2, [4, 5]),
        ([1], 1, [1]),
        ([1, 1, 2, 2, 3, 3, 4, 4, 5], 3, [1, 2, 3])
    ]

    # Instantiate the solution class
    solution = Solution()

    # Run tests for the bucket sort solution
    for i, (nums, k, expected) in enumerate(test_cases):
        result = solution.topKFrequent(nums, k)
        assert set(result) == set(expected), \
            f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All bucket sort tests passed!")

    # Run tests for the heap-based solution
    for i, (nums, k, expected) in enumerate(test_cases):
        result = solution.topKFrequentHeap(nums, k)
        assert set(result) == set(expected), \
            f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All heap tests passed!")
