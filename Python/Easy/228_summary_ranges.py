from typing import List

class Solution:
    """
    A class to solve the 'Summary Ranges' problem.

    Problem:
        Given a sorted unique integer array `nums`, return the smallest sorted list of ranges that 
        cover all the numbers in the array exactly. Each range `[a,b]` in the list should be output as:
        - "a->b" if a != b
        - "a" if a == b

        Example 1:
            Input: nums = [0,1,2,4,5,7]
            Output: ["0->2","4->5","7"]

        Example 2:
            Input: nums = [0,2,3,4,6,8,9]
            Output: ["0","2->4","6","8->9"]

    Constraints:
        - 0 <= nums.length <= 20
        - -2^31 <= nums[i] <= 2^31 - 1
        - All the values of `nums` are unique.
        - `nums` is sorted in ascending order.
    """

    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Finds the summary ranges in a sorted unique integer array.

        This method uses a `range(N-1)` loop to iterate through the array and checks if the current 
        number and the next number are consecutive. If not, it forms a range and starts a new one.

        Args:
            nums (List[int]): A sorted list of unique integers.

        Returns:
            List[str]: A list of strings representing the smallest sorted list of ranges that cover 
            all the numbers in the array exactly.

        Time Complexity:
            O(N), where N is the length of the input list. The function iterates through the list once.

        Space Complexity:
            O(1), not including the space required for the output list.
        """
        if not nums:
            return []

        N: int = len(nums)
        ranges: List[str] = []
        start: int = nums[0]
        stop: int = 0
        
        for n in range(N-1):
            diff: int = nums[n+1] - nums[n]
            if diff > 1:
                stop = nums[n]
                if start != stop:
                    ranges.append(f"{start}->{stop}")
                else:
                    ranges.append(f"{start}")
                start = nums[n+1]
        
        stop = nums[-1]
        if start != stop:
            ranges.append(f"{start}->{stop}")
        else:
            ranges.append(f"{stop}")
        
        return ranges

    def summaryRangesAlternative(self, nums: List[int]) -> List[str]:
        """
        Finds the summary ranges in a sorted unique integer array using a `range(1, N)` loop.

        This method uses a `range(1, N)` loop to iterate through the array, which simplifies the 
        logic by directly comparing each element with the previous one. This method is generally 
        more intuitive and reduces the chance of off-by-one errors.

        Args:
            nums (List[int]): A sorted list of unique integers.

        Returns:
            List[str]: A list of strings representing the smallest sorted list of ranges that cover 
            all the numbers in the array exactly.

        Advantages:
            - The `range(1, N)` loop ensures that all elements are considered and simplifies the logic 
              of comparing consecutive elements.
            - This approach reduces the complexity of handling edge cases such as single-element lists 
              or the last range in the list.

        Time Complexity:
            O(N), where N is the length of the input list. The function iterates through the list once.

        Space Complexity:
            O(1), not including the space required for the output list.
        """
        if not nums:
            return []

        N: int = len(nums)
        ranges: List[str] = []
        start: int = nums[0]
        
        for i in range(1, N):
            if nums[i] != nums[i-1] + 1:
                if start != nums[i-1]:
                    ranges.append(f"{start}->{nums[i-1]}")
                else:
                    ranges.append(f"{start}")
                start = nums[i]
        
        if start != nums[-1]:
            ranges.append(f"{start}->{nums[-1]}")
        else:
            ranges.append(f"{start}")
        
        return ranges
    
    def summaryRangesMap(self, nums: List[int]) -> List[str]:
        """
        An alternative implementation using the map function to improve code readability.

        This method uses map to identify breaks in the consecutive sequence and then groups the 
        ranges accordingly.

        Args:
            nums (List[int]): A sorted list of unique integers.

        Returns:
            List[str]: A list of strings representing the smallest sorted list of ranges that cover 
            all the numbers in the array exactly.

        Time Complexity:
            O(N), where N is the length of the input list. The function iterates through the list once.

        Space Complexity:
            O(1), not including the space required for the output list.
        """
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i, n in enumerate(map(lambda i: nums[i] - nums[i-1], range(1, len(nums)))):
            if n > 1:
                if start != nums[i]:
                    ranges.append(f"{start}->{nums[i]}")
                else:
                    ranges.append(f"{start}")
                start = nums[i+1]

        # Add the last range
        if start != nums[-1]:
            ranges.append(f"{start}->{nums[-1]}")
        else:
            ranges.append(f"{start}")

        return ranges


if __name__ == "__main__":
    # Test cases with expected outcomes
    test_cases = [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
        ([0], ["0"]),
        ([0, 1], ["0->1"]),
        ([0, 2], ["0", "2"]),
        ([], []),
    ]

    # Initialise the Solution class
    solution = Solution()

    # Run the test cases for both methods
    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.summaryRanges(nums) == expected, f"Method 1, Test case {i} failed"
        assert solution.summaryRangesAlternative(nums) == expected, f"Method 2, Test case {i} failed"
        assert solution.summaryRangesMap(nums) == expected, f"Method 3, Test case {i} failed"

    print("All test cases passed!")