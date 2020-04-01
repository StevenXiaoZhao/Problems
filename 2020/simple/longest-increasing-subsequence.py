from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = len(nums)
        length = [0] * count

        for i in range(0, count):
            length[i] = 1
            for j in range(i):
                if nums[i] > nums[j] and length[j] > length[i]:
                    length[i] = length[j] + 1

        return max(length) if count > 0 else 0


print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
