from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        max_area = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(0, m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue

                grid[i][j] = -1
                queue = set()
                area = 1
                if i + 1 < m and grid[i + 1][j] == 1:
                    queue.add((i + 1, j))

                if j + 1 < n and grid[i][j + 1] == 1:
                    queue.add((i, j + 1))
                while len(queue) > 0:
                    point_i, point_j = queue.pop()
                    area += 1
                    grid[point_i][point_j] = area
                    if point_i + 1 < m and grid[point_i + 1][point_j] == 1:
                        queue.add((point_i + 1, point_j))
                    if point_i - 1 >= 0 and grid[point_i - 1][point_j] == 1:
                        queue.add((point_i - 1, point_j))
                    if point_j + 1 < n and grid[point_i][point_j + 1] == 1:
                        queue.add((point_i, point_j + 1))
                    if point_j - 1 >= 0 and grid[point_i][point_j - 1] == 1:
                        queue.add((point_i, point_j - 1))

                if area > max_area:
                    max_area = area

        return max_area


test = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution().maxAreaOfIsland(test))
print(test)
