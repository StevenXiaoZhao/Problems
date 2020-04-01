from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if nums is None or len(nums) == 0:
            return

        zero_count = 0
        count = len(nums)
        for i in range(count):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i - zero_count] = nums[i]

        while zero_count > 0:
            nums[count - zero_count] = 0
            zero_count -= 1


t = [0, 0, 0, 6,12, 4,5]
Solution().moveZeroes(t)
print(t)
