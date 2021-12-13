from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n-1
        while i <= j:
            k = int((i+j)/2)
            if nums[k] == target:
                return k
            elif nums[k] > target:
                j = k-1
            else:
                i = k+1

        return -1

print(Solution().search(

nums = [5], target = 5
))