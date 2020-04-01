from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        count = len(A)
        if count <= 1:
            return 0

        result = 0
        dup = []
        for i in range(1, count):
            if A[i] == A[i - 1]:
                dup.append(A[i])
            elif A[i] - A[i - 1] > 1 and len(dup) > 0:
                span = A[i - 1] + 1
                while span < A[i] and len(dup) > 0:
                    result += span - dup.pop(0)
                    span += 1
        last = A[-1] + 1
        while len(dup) > 0:
            result += last - dup.pop(0)
            last+=1

        return result


print(Solution().minIncrementForUnique([2,2,2,1]))
