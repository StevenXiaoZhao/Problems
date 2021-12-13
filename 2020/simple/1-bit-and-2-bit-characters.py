from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        if n == 1:
            return True
        i = 0
        is_one = True
        while i < n :
            if bits[i] == 0:
                i+=1
                is_one = True
            else:
                i+=2
                is_one = False
        return is_one

print(Solution().isOneBitCharacter(bits = [0]))
