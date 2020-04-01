from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                left = 0 if i - 1 < 0 else grid[i - 1][j]
                right = 0 if i + 1 >= m else grid[i + 1][j]
                up = 0 if j - 1 < 0 else grid[i][j - 1]
                down = 0 if j + 1 >= n else grid[i][j + 1]
                result += 4 - (left + right + up + down)
        return result


print(Solution().islandPerimeter([[0, 1, 0, 0],
                                  [1, 1, 1, 0],
                                  [0, 1, 0, 0],
                                  [1, 1, 0, 0]]))
