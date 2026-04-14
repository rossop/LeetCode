

class Solution:
        def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
            res: int = len(nums)
            for i, num in enumerate(nums):
                if num == target:
                    res = min(res, abs(i -start))

            return res


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "nums":[1,2,3,4,5],
            "target": 5,
            "start": 3,
            "output": 1
        },
        {
            "nums":[1],
            "target": 1,
            "start": 0,
            "output": 0
        },
        {
            "nums":[1,1,1,1,1,1,1,1,1,1,],
            "target": 1,
            "start": 0,
            "output": 0
        },
    ]

    num_of_tests: int = len(test_cases)
    num_of_passed_tests : int = 0
    for ii, var_dicts in enumerate(test_cases):
        nums: list[int] = var_dicts.get("nums", [])
        target: int = var_dicts.get("target", 0)
        start: int = var_dicts.get("start", 0)
        output: int = var_dicts.get("output", 0)
        if solution.getMinDistance(nums, target, start) == output:
            num_of_passed_tests += 1
            print(f"Pass test number {ii}")
        else:
            print(f"Failed test number {ii}")



    if num_of_tests == num_of_passed_tests:
        print("All test cases passed!")
