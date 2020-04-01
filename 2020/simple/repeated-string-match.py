import math


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if len(B) < len(A):
            if A.find(B) != -1:
                return 1

            A = A*2
            return 2 if A.find(B) != -1 else -1
        else:
            count = math.ceil(len(B) / len(A))
            C = A * count
            i = 0
            while i < 3:
                C += A * i
                if C.find(B) != -1:
                    return count + i
                i += 1

        return -1


print(Solution().repeatedStringMatch(A="abcd", B="da"))
