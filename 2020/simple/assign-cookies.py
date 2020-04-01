from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g is None or s is None:
            return 0
        g.sort()
        s.sort()

        count_g = len(g)
        count_s = len(s)
        i = 0
        j = 0
        result = 0
        while i < count_g and j < count_s:
            if g[i] <= s[j]:
                i += 1
                j += 1
                result += 1
            else:
                j += 1
        return result


print(Solution().findContentChildren([], []))
