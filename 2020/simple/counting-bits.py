from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_count = [0]
        if n == 0:
            return bit_count

        bit_count.append(1)
        if n == 1:
            return bit_count

        base = 2
        for i in range(2, n + 1):
            if i == base:
                base = base * 2
                bit_count.append(1)
            else:
                bit_count.append(1 + bit_count[i - base])

        return bit_count

print(Solution().countBits(7))