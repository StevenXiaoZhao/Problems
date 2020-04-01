from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums is None or len(nums) ==0:
            return False

        t = set(nums)
        return len(t)!= len(nums)