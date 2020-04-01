from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) ==0:
            return 0
        count = len(nums)
        length = 1
        max_len = 1
        for i in range(1, count):
            if nums[i]> nums[i-1]:
                length+=1
            else:
                if length > max_len:
                    max_len = length
                length =1

        if length> max_len:
            max_len = length

        return max_len

print(Solution().findLengthOfLCIS([1,1,1]))