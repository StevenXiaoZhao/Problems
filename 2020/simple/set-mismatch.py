from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = len(nums)
        sum_nums = sum(nums)
        sum_nums_set = sum(set(nums))
        duplicate = sum_nums - sum_nums_set
        missing = int((count+1)*count/2)
        return [duplicate, duplicate + missing-sum_nums]

print(Solution().findErrorNums(nums = [2,2]))