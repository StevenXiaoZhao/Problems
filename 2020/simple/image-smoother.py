from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:

        m = len(M)
        if m == 0:
            return M
        n = len(M[0])
        if m * n == 1:
            return M

        result = []
        for i in range(m):
            result.append([0]*n)

        for i in range(m):
            for j in range(n):
                temp = 0
                count = 0
                for t in range(i - 1, i + 2):
                    if 0 <= t < m:
                        for p in range(j - 1, j + 2):
                            if 0 <= p < n:
                                temp += M[t][p]
                                count += 1

                result[i][j] = int(temp / count)

        return result


print(Solution().imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))
