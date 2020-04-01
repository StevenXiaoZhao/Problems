from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <=2:
            return True

        count = len(nums)
        occurs = False
        for i in range(0, count-1):
            if nums[i]<=nums[i+1]:
                continue

            if occurs:
                return False

            occurs = True
            if i==0:
                nums[i] = nums[i+1]
            else:
                if nums[i+1] >= nums[i-1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        return True

test = [-1,4,2,3]
print(Solution().checkPossibility(test))
print(test)
