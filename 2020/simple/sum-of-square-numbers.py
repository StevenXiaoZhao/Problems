import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_factor = int(math.sqrt(c/2))
        for i in range(max_factor+1):
            num = c-i*i
            factor = int(math.sqrt(num))
            if factor*factor == num:
                return True

        return False

print(Solution().judgeSquareSum(3))