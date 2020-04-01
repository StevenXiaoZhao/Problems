from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k])
        curr_total = total
        count = len(nums)
        for i in range(k, count):
            curr_total += nums[i]-nums[i-k]
            if curr_total > total:
                total = curr_total

        return total/k

print(Solution().findMaxAverage([1,12,-5,-6,50,3], k = 4))
