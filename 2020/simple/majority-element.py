from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        present_val = nums[0]
        for num in nums:
            if count ==0:
                count=1
                present_val = num
            elif num == present_val:
                count+=1
            else:
                count-=1
                present_val = num

        return present_val