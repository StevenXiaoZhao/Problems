from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = len(nums)
        if count <= 1:
            return count

        new_index = 1
        for i in range(1, count):
            if nums[i] != nums[i-1]:
                nums[new_index] = nums[i]
                new_index+=1
        return new_index

arr = [0,1]
print(Solution().removeDuplicates(arr))
print(arr)

