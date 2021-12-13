from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        min_significant_bit = xor & (-xor)
        x = 0
        y = 0
        for num in nums:
            if min_significant_bit & num == min_significant_bit:
                x ^= num
            else:
                y ^= num
        return [x, y]

print(Solution().singleNumber([1,2,1,3,2,5]))
