from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        m_min = float('inf')
        n_min = float('inf')
        for op in ops:
            if m_min > op[0]:
                m_min = op[0]

            if n_min > op[1]:
                n_min = op[1]
        if m < m_min:
            m_min = m

        if n < n_min:
            n_min = n

        return m_min * n_min

print(Solution().maxCount(m = 3, n = 3, ops = [[2,2],[3,3]]))
