from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of `candidates` where the sum equals the `target`, and each number 
        in `candidates` may only be used once in the combination. The solution set must not contain duplicate 
        combinations. This solution uses a `while` loop to skip over duplicates before exploring branches.

        Args:
            candidates (List[int]): A list of candidate numbers.
            target (int): The target sum to achieve.

        Returns:
            List[List[int]]: A list of all unique combinations that sum up to the target.

        Time Complexity:
            O(2^n): In the worst case, where n is the number of candidates. The backtracking explores all 
            possible combinations of candidates.

        Space Complexity:
            O(n): The maximum depth of the recursion tree is proportional to the number of candidates.
        """
        res: List[List[int]] = []
        sol: List[int] = []
        nums = sorted(candidates)
        n = len(nums)

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol.copy())
                return  
            
            if cur_sum > target or i >= n:
                return

            # Skip duplicates using a while loop
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            backtrack(j, cur_sum)

            # Include the current number
            sol.append(nums[i])
            backtrack(i + 1, cur_sum + nums[i])
            sol.pop()

        backtrack(0, 0)
        res.sort()
        return res

    
    def combinationSum2ForLoop(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        This solution finds all unique combinations of `candidates` where the sum equals the `target`, using 
        a `for` loop to handle duplicate elements and prevent the same combination from being generated multiple times.

        The key difference from the `while` loop variant is that the `for` loop inherently handles the traversal 
        of the candidate numbers and skips over duplicates by checking the current number against the previous one.

        Args:
            candidates (List[int]): A list of candidate numbers.
            target (int): The target sum to achieve.

        Returns:
            List[List[int]]: A list of all unique combinations that sum up to the target.

        Time Complexity:
            O(2^n): Similar to the `while` loop variant, the backtracking explores all possible combinations.

        Space Complexity:
            O(n): The maximum depth of the recursion tree is proportional to the number of candidates.

        Comparison to the `while` loop solution:
            - The `for` loop variant is slightly easier to understand and implement because it directly iterates over 
              candidates, automatically managing the index increment and ensuring that the next number is considered.
            - The `while` loop solution explicitly controls the index and can sometimes provide a bit more flexibility 
              in how duplicates are skipped, but it requires careful management of indices to avoid errors.
            - Both methods have the same time and space complexity, but the `for` loop solution might be more intuitive 
              for handling problems where you need to iterate over elements and conditionally skip duplicates.
        """
        res: List[List[int]] = []
        sol: List[int] = []
        nums = sorted(candidates)
        n = len(nums)

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol.copy())
                return  
            
            if cur_sum > target or i >= n:
                return

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                sol.append(nums[j])
                backtrack(j + 1, cur_sum + nums[j])
                sol.pop()

        backtrack(0, 0)
        res.sort()
        return res


if __name__ == "__main__":
    solution = Solution()

    # Test cases for the while loop variant
    assert solution.combinationSum2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]]
    assert solution.combinationSum2([2,5,2,1,2], 5) == [[1,2,2],[5]]

    # Test cases for the for loop variant
    assert solution.combinationSum2ForLoop([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]]
    assert solution.combinationSum2ForLoop([2,5,2,1,2], 5) == [[1,2,2],[5]]

    print("All test cases passed!")