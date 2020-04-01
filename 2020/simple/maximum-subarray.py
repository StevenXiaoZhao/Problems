from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        max_sum = float('-inf')
        sub_sum = 0
        count = len(nums)
        above_zero = False
        for i in range(0, count):
            if above_zero and nums[i] < 0:
                if sub_sum > max_sum:
                    max_sum = sub_sum
                above_zero = False
            elif not above_zero:
                if nums[i] > 0:
                    above_zero = True
                    if sub_sum < 0:
                        sub_sum = 0
                elif nums[i] > max_sum:  # 数组里有可能都是负数
                    max_sum = nums[i]

            sub_sum += nums[i]
        if sub_sum > max_sum:
            max_sum = sub_sum

        return max_sum

print(Solution().maxSubArray([-2,1]))
