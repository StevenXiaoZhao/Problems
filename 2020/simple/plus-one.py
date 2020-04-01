from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        left = 1
        count = len(digits)
        for i in range(count):
            val = digits[count-1-i]
            result = val + left
            digits[count-1-i] = result%10
            left = int(result/10)
        if left>0:
            return [left] + digits
        else:
            return digits

print(Solution().plusOne([0]))