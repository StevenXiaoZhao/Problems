import math
class Solution:
    def reverse(self, x: int) -> int:
        isAboveZero = (x > 0)
        if isAboveZero is False:
            x = -x

        result = 0
        while x > 0:
            num = x % 10
            result = result * 10 + num
            x = math.floor(x/10)

        if isAboveZero is False:
            result = -result

        max_value = 1024*1024*1024*2
        if result >= max_value -1 or result <= -max_value:
            return 0
        return result

print(Solution().reverse(-2147483412))