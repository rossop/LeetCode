from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the characters in the input list in place using the two-pointer technique.

        This method modifies the input list `s` by reversing its elements in place. The 
        two-pointer approach is used, where pointers start at both ends of the list and 
        move towards the center, swapping elements at each step.

        This method has O(n) time complexity and O(1) space complexity, making it very 
        efficient for reversing large lists. It is preferred in algorithmic problem-solving 
        due to its explicit demonstration of the logic involved in reversing a string.

        Args:
            s (List[str]): A list of characters representing the string to be reversed.

        Returns:
            None: The function does not return anything. The input list `s` is modified in place.

        Time Complexity:
            O(n): We traverse the entire list once, with each element being processed exactly once.

        Space Complexity:
            O(1): The reversal is done in place without using extra space proportional to the input size.

        Example:
            s = ["h","e","l","l","o"]
            reverseString(s)
            print(s)  # Output: ["o","l","l","e","h"]

        Constraints:
            - The length of `s` is between 1 and 10^5 inclusive.
            - Each element in `s` is a printable ASCII character.
        """
        n = len(s)
        L: int = 0
        R: int = n - 1
        
        while L < R:
            # Swap characters
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1

    def reverseStringAlternative(self, s: List[str]) -> None:
        """
        Reverses the characters in the input list using the built-in reverse method.

        This method is a simple and Pythonic way to reverse the elements in a list by 
        using the built-in `reverse()` method, which operates in place.

        While it has the same time and space complexity as the two-pointer approach,
        it abstracts away the mechanics of the reversal, making it less suitable for 
        educational purposes in algorithm studies.

        Args:
            s (List[str]): A list of characters representing the string to be reversed.

        Returns:
            None: The function does not return anything. The input list `s` is modified in place.

        Time Complexity:
            O(n): The `reverse()` method internally iterates over the list once.

        Space Complexity:
            O(1): The reversal is done in place with no extra space needed.

        Comparison with Two-Pointer Approach:
            - Both methods have the same time complexity of O(n).
            - Both methods have the same space complexity of O(1).
            - The two-pointer approach is often preferred in algorithmic problem-solving contexts
              because it explicitly demonstrates the logic and understanding of the problem, 
              which is valuable in interview scenarios and educational purposes.
            - The `reverse()` method is more concise and Pythonic but may be less instructive.
        """
        s.reverse()

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases and their expected outputs
    test_cases = [
        (["h","e","l","l","o"], ["o","l","l","e","h"]),
        (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]),
        (["A"], ["A"]),
        ([], []),
        (["p","y","t","h","o","n"], ["n","o","h","t","y","p"])
    ]

    # Testing the reverseString method
    for i, (input_str, expected) in enumerate(test_cases):
        solution.reverseString(input_str)
        assert input_str == expected, f"Test case {i+1} failed: expected {expected}, got {input_str}"

    # Alternative method test
    alt_test_case = ["h","e","l","l","o"]
    alt_expected = ["o","l","l","e","h"]
    solution.reverseStringAlternative(alt_test_case)
    assert alt_test_case == alt_expected, f"Alternative method test failed: expected {alt_expected}, got {alt_test_case}"

    print("All test cases passed!")