from typing import List
    # def removeDuplicates(self, nums: List[int]) -> int:
nums = [0,0,1,1,1,2,2,3,3,4]
revised_nums =[]
if not nums:
    print(len(revised_nums))
for n in nums[1:]:
    if revised_nums:
        if n != revised_nums[-1]:
            revised_nums.append(n)
    else:
        revised_nums.append(n)

print(len(revised_nums))