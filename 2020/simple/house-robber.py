from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        if len(nums) == 0:
            return 0
        elif len(nums)  ==1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] >= nums[1] else nums[1]

        a = nums[0]
        b = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            c = max(nums[i]+a, b)
            a=b
            b=c
        return c
        #return self.robMax(nums, len(nums)-1)

    def robMax(self, nums: List[int], n)->int:
        if n<0:
            return 0

        result1 = nums[n] + self.robMax(nums, n-2)
        result2 = self.robMax(nums, n-1)
        return result1 if result1>=result2 else result2

t= [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
#t= [2,1,1,2]
print(Solution().rob(t))