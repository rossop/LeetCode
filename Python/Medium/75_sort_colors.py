from typing import List

class Solution:
    def sortColorsCounting(self, nums: List[int]) -> None:
        """
        Sorts the input list `nums` which contains only 0s, 1s, and 2s (representing colors)
        using the counting sort approach. This function modifies the list in-place.

        Time Complexity:
            O(n): We iterate over the list to count the number of 0s, 1s, and 2s, and then 
            iterate again to overwrite the list with the sorted order.

        Space Complexity:
            O(1): This solution uses a fixed amount of extra space (counters and index), 
            independent of the input size.

        Args:
            nums (List[int]): The list of integers (0, 1, 2) representing colors to be sorted.
        
        Returns:
            None: The function modifies `nums` in-place.
        """
        c0 = 0
        c1 = 0
        c2 = 0

        # Count 0s, 1s and 2s
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1

        idx = 0
        # Place all the 0s
        for i in range(c0):
            nums[idx] = 0
            idx += 1

        # Place all the 1s
        for i in range(c1):
            nums[idx] = 1
            idx += 1

        # Place all the 2s
        for i in range(c2):
            nums[idx] = 2
            idx += 1

    def sortColorsSlicing(self, nums: List[int]) -> None:
        """
        Sorts the input list `nums` which contains only 0s, 1s, and 2s (representing colors)
        using a slicing approach. This function modifies the list in-place.

        Time Complexity:
            O(n): Similar to the counting approach, we iterate over the list to count the 
            number of 0s, 1s, and 2s, and then we overwrite slices of the list with the sorted values.

        Space Complexity:
            O(1): This solution also uses a fixed amount of extra space, as it modifies the 
            list in-place using slicing.

        Args:
            nums (List[int]): The list of integers (0, 1, 2) representing colors to be sorted.

        Returns:
            None: The function modifies `nums` in-place.
        """
        c0 = 0
        c1 = 0
        c2 = 0

        # Count 0s, 1s and 2s
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1

        nums[:c0] = [0] * c0
        nums[c0:c1 + c0] = [1] * c1
        nums[c0 + c1:c0 + c1 + c2] = [2] * c2


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([2, 2, 2], [2, 2, 2])
    ]

    for i, (input_list, expected) in enumerate(test_cases):
        nums1 = input_list.copy()
        nums2 = input_list.copy()

        solution.sortColorsCounting(nums1)
        solution.sortColorsSlicing(nums2)

        assert nums1 == expected, f"Test case {i + 1} failed for sortColorsCounting: expected {expected}, got {nums1}"
        assert nums2 == expected, f"Test case {i + 1} failed for sortColorsSlicing: expected {expected}, got {nums2}"

    print("All test cases passed!")

    # Additional test for performance and edge cases
    large_test = [2] * 100 + [1] * 100 + [0] * 100
    sorted_large_test = [0] * 100 + [1] * 100 + [2] * 100

    nums1 = large_test.copy()
    nums2 = large_test.copy()

    solution.sortColorsCounting(nums1)
    solution.sortColorsSlicing(nums2)

    assert nums1 == sorted_large_test, "Large test case failed for sortColorsCounting"
    assert nums2 == sorted_large_test, "Large test case failed for sortColorsSlicing"

    print("Large test case passed!")