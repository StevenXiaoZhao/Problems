from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_val = max(nums)
        max_val_index = nums.index(max_val)
        nums.remove(max_val)
        max_val_2 = max(nums)
        if max_val >= max_val_2 * 2:
            return max_val_index

        return -1

print(Solution().dominantIndex(nums = [1]))