from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            index = nums[i] if nums[i] > 0 else -nums[i]
            index -= 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        result = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
