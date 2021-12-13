from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        return nums+nums


print(Solution().getConcatenation([]))