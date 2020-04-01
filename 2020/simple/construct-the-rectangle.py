from typing import List
import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a = int(math.sqrt(area))
        b = int(area / a)
        if b > a:
            a, b = b, a
        while b * a != area:
            a += 1
            b = int(area / a)

        return [a, b]


print(Solution().constructRectangle(89374855))
