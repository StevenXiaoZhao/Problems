from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start_index = 0
        if nums is None or len(nums) == 0:
            return 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[start_index] = nums[i]
                start_index += 1

        return start_index


test = [0,1,2,2,3,0,4,2]
val = 2
result = Solution().removeElement(test, val)
print(result)
print(test)
