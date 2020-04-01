from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        curr = A[0]
        for i in range(1, len(A)):
            if A[i] == curr:
                return curr

        curr = A[1]
        for i in range(2, len(A)):
            if A[i] == curr:
                return curr
            else:
                curr = A[i]

        return A[-1]