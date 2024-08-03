from typing import List

class Solution:
    """
    A class to solve the 'Combination Sum' problem.

    Problem:
        Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. The same number may be chosen from candidates an unlimited number of times. You may return the combinations in any order.

        The test cases are generated such that the number of unique combinations that sum up to `target` is less than 150 combinations for the given input.

    Example 1:
        Input: candidates = [2,3,6,7], target = 7
        Output: [[2,2,3],[7]]
        Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.

    Example 2:
        Input: candidates = [2,3,5], target = 8
        Output: [[2,2,2,2],[2,3,3],[3,5]]

    Example 3:
        Input: candidates = [2], target = 1
        Output: []

    Constraints:
        - 1 <= candidates.length <= 30
        - 2 <= candidates[i] <= 40
        - All elements of candidates are distinct.
        - 1 <= target <= 40
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of `candidates` where the sum equals the `target`. Each candidate can be used an unlimited number of times.

        Args:
            candidates (List[int]): A list of distinct integers to be combined.
            target (int): The target sum to be achieved.

        Returns:
            List[List[int]]: A list of lists, where each inner list is a unique combination of numbers that sum to `target`.
        """
        res: List[List[int]] = []  # list to store all valid combinations
        sol: List[int] = []  # temporary list to store the current combination
        nums = candidates
        n = len(nums)

        def backtrack(i: int, cur_sum: int) -> None:
            """
            A helper function to perform the backtracking algorithm.

            Args:
                i (int): The current index in `candidates`.
                cur_sum (int): The current sum of the combination being formed.

            Returns:
                None
            """
            # Base case: If the current sum equals the target, add the combination to the result list
            if cur_sum == target:
                res.append(sol[:])  # Make a copy of the current solution
                return
            
            # Base case: If the current sum exceeds the target or we've exhausted all candidates, return
            if cur_sum > target or i >= n:
                return
            
            # Explore the branch where we don't include the current candidate
            backtrack(i + 1, cur_sum)

            # Explore the branch where we include the current candidate
            sol.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            sol.pop()  # Backtrack by removing the last added candidate from the solution

        # Start the backtracking process
        backtrack(0, 0)
        return res


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
        ([2], 1, []),
        ([2,3,5,7], 7, [[2,2,3],[7], [2,5]])
    ]

    # Assert the validity of the answers
    for i, (candidates, target, expected) in enumerate(test_cases, 1):
        result = solution.combinationSum(candidates, target)
        assert sorted(result) == sorted(expected), f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed: {result}")

    print("All test cases passed!")