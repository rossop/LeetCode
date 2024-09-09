class Solution:
    """
    A class to solve the 'Jewels and Stones' problem.

    Problem:
        You're given strings `jewels` representing the types of stones that are jewels, 
        and `stones` representing the stones you have. Each character in `stones` is a 
        type of stone you have. You want to know how many of the stones you have are 
        also jewels.

        Letters are case sensitive, so "a" is considered a different type of stone from "A".

    Example 1:
        Input: jewels = "aA", stones = "aAAbbbb"
        Output: 3

    Example 2:
        Input: jewels = "z", stones = "ZZ"
        Output: 0

    Constraints:
        - 1 <= jewels.length, stones.length <= 50
        - `jewels` and `stones` consist of only English letters.
        - All the characters of `jewels` are unique.
    """

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Counts how many of the stones you have are also jewels.

        Args:
            jewels (str): A string representing the types of stones that are jewels.
            stones (str): A string representing the stones you have.

        Returns:
            int: The number of stones that are also jewels.

        Time Complexity:
            O(n * m): In the worst case, where n is the length of `stones` and m is the length of `jewels`.
                      For each stone, it checks if it is in jewels, resulting in n*m operations.
                      
        Space Complexity:
            O(1): Since we are only using a fixed amount of extra space.
        """
        counter = 0
        for s in stones:
            if s in jewels:
                counter += 1
        return counter

    def numJewelsInStonesOptimized(self, jewels: str, stones: str) -> int:
        """
        Optimized version of `numJewelsInStones` using a set for `jewels` to reduce lookup time.

        Args:
            jewels (str): A string representing the types of stones that are jewels.
            stones (str): A string representing the stones you have.

        Returns:
            int: The number of stones that are also jewels.

        Time Complexity:
            O(n): Where n is the length of `stones`. Each stone is checked in O(1) time using the set.
                      
        Space Complexity:
            O(m): Where m is the length of `jewels`. The set used for `jewels` requires O(m) space.
        """
        jewel_set = set(jewels)
        return sum(s in jewel_set for s in stones)


if __name__ == "__main__":
    solution = Solution()

    # Test cases for the original solution
    assert solution.numJewelsInStones("aA", "aAAbbbb") == 3
    assert solution.numJewelsInStones("z", "ZZ") == 0

    # Test cases for the optimized solution
    assert solution.numJewelsInStonesOptimized("aA", "aAAbbbb") == 3
    assert solution.numJewelsInStonesOptimized("z", "ZZ") == 0

    print("All test cases passed!")