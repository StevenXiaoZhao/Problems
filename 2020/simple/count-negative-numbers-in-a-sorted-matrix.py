from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        return self.countMatrixNegatives(grid, 0, 0, m - 1, n - 1)

    def countMatrixNegatives(self, grid: List[List[int]], s_i, s_j, e_i, e_j) -> int:
        if s_i == e_i and s_j == e_j:
            return 1 if grid[s_i][s_j] < 0 else 0

        if s_i > e_i or s_j > e_j:
            return 0

        if grid[s_i][s_j] < 0:
            return (e_i + 1 - s_i) * (e_j + 1 - s_j)

        if grid[e_i][e_j] >= 0:
            return 0
        mid_i = int((s_i + e_i) / 2)
        mid_j = int((s_j + e_j) / 2)
        return self.countMatrixNegatives(grid, s_i, s_j, mid_i, mid_j) \
               + self.countMatrixNegatives(grid, s_i, mid_j + 1, mid_i, e_j) \
               + self.countMatrixNegatives(grid, mid_i + 1, s_j, e_i, mid_j) \
               + self.countMatrixNegatives(grid, mid_i + 1, mid_j + 1, e_i, e_j)


print(Solution().countNegatives(grid=[[7, -3]]))
