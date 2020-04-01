from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #每次给n-1个值加1，就相当于给1个值减一，一直减到大家一样
        return sum(nums)-len(nums)*min(nums)
print(Solution().minMoves([200,0,100]))