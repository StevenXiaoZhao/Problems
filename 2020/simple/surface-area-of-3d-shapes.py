from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                result += 4 * grid[i][j] + 2 if grid[i][j] > 0 else 0

                result -= min(grid[i][j], grid[i][j - 1] if j > 0 else 0)
                result -= min(grid[i][j], grid[i - 1][j] if i > 0 else 0)
                result -= min(grid[i][j], grid[i][j + 1] if j < n - 1 else 0)
                result -= min(grid[i][j], grid[i + 1][j] if i < m - 1 else 0)

        return result


print(Solution().surfaceArea([[1,2],[3,4]]))
