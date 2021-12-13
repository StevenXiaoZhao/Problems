from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        total_left = 0
        total_right = total
        for i in range(len(nums)):
            num = nums[i]
            total_right -= num

            if total_left == total_right:
                return i
            else:
                total_left += num
        return -1


print(Solution().pivotIndex(nums = [1, 2, 3]))