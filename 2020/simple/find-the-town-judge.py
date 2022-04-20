from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_others = [0] * (n + 1)
        be_trusted = [0] * (n + 1)
        for pair in trust:
            fr = pair[0]
            to = pair[1]
            trust_others[fr] += 1
            be_trusted[to] += 1

        for i in range(1, n + 1):
            if be_trusted[i] == n - 1 and trust_others[i] == 0:
                return i

        return -1


print(Solution().findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
