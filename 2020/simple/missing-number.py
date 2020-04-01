from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        total = sum(nums)
        result = int((count+1)*count/2)
        return result - total

print(Solution().missingNumber([3,0,1]))