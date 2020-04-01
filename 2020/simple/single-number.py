from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1]^nums[i]

        return nums[len(nums)-1]

print(Solution().singleNumber([4,1,2,1,2,4,10]))