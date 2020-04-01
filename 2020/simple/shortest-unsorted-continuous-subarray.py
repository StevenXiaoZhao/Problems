from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        nums_copy = nums.copy()
        nums_copy.sort()
        count = len(nums)

        left = 0
        right = count-1
        while left < count:
            if nums[left] == nums_copy[left]:
                left+=1
            else:
                break
        while right>=left:
            if nums[right] == nums_copy[right]:
                right-=1
            else:
                break

        return right - left+1


print(Solution().findUnsortedSubarray([4,3,2,1,0,7,8,9,10,11,12,13]))
