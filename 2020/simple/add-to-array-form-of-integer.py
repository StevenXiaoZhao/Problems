from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        left = 0
        more = []
        count = len(A)
        for i in range(count):
            current_value = A[count-1-i]
            k_v = K%10
            K = int(K/10)
            value = k_v + current_value + left
            left = int(value/10)
            A[count-1-i] = value%10

        if K == 0:
            if left > 0:
                more = [left]
        elif K > 0:
            left_value = left + K
            while left_value > 0:
                more.append(left_value%10)
                left_value = int(left_value/10)
        more.reverse()
        return more + A

print(Solution().addToArrayForm([], 1))