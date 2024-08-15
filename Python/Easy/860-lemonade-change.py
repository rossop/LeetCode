from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Determines if we can provide the correct change for every customer in line.
        
        The function tracks the number of $5 and $10 bills available and uses them
        to provide change as needed. It prioritizes using a $10 bill and a $5 bill
        to make change for a $20 bill, as this preserves more $5 bills for future use.

        Time Complexity:
            O(n): The function iterates through the list of bills once, where `n` is the number of customers.
        
        Space Complexity:
            O(1): The function uses a constant amount of extra space (only a few integer variables).
        
        Args:
            bills (List[int]): A list of integers where each element is either 5, 10, or 20, representing the bills given by customers.
        
        Returns:
            bool: Returns True if all customers can be provided with the correct change, otherwise False.
        """
        counter: List[int] = [0, 0]  # counter[0]: $5 bills, counter[1]: $10 bills
        
        for b in bills:
            if b == 5:
                counter[0] += 1
            elif b == 10:
                if counter[0] > 0:
                    counter[0] -= 1
                    counter[1] += 1
                else:
                    return False
            elif b == 20:
                # Priority: Give one $10 and one $5 as change
                if counter[1] > 0 and counter[0] > 0:
                    counter[1] -= 1
                    counter[0] -= 1
                # Otherwise, give three $5 as change
                elif counter[0] >= 3:
                    counter[0] -= 3
                else:
                    return False
        
        return True

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        ([5, 5, 5, 10, 20], True),
        ([5, 5, 10, 10, 20], False),
        ([5, 5, 10], True),
        ([10, 10], False),
        ([5, 5, 5, 5, 10, 5, 10, 10, 10, 20], True),
        ([5, 10, 20], False),
        ([5, 5, 5, 10, 10, 20], True)
    ]

    for i, (bills, expected) in enumerate(test_cases):
        result = solution.lemonadeChange(bills)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases passed!")