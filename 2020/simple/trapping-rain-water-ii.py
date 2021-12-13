from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        left_side_max_map = [[0] * n for _ in range(m)]
        right_side_max_map = [[0] * n for _ in range(m)]
        up_side_max_map = [[0] * n for _ in range(m)]
        down_side_max_map = [[0] * n for _ in range(m)]

        # left max
        for i in range(m):
            left_max = heightMap[i][0]
            for j in range(1, n):
                left_side_max_map[i][j] = left_max
                if heightMap[i][j] > left_max:
                    left_max = heightMap[i][j]

        # right max
        for i in range(m):
            right_max = heightMap[i][-1]
            for j in range(n - 2, -1, -1):
                right_side_max_map[i][j] = right_max
                if heightMap[i][j] > right_max:
                    right_max = heightMap[i][j]

        # up max
        for j in range(n):
            up_max = heightMap[0][j]
            for i in range(1, m):
                up_side_max_map[i][j] = up_max
                if heightMap[i][j] > up_max:
                    up_max = heightMap[i][j]

        # down max
        for j in range(n):
            down_max = heightMap[-1][j]
            for i in range(m - 2, -1, -1):
                down_side_max_map[i][j] = down_max
                if heightMap[i][j] > down_max:
                    down_max = heightMap[i][j]
        # 计算洼地的水量
        total_rain = 0
        for i in range(m):
            for j in range(n):
                rain_level = min(left_side_max_map[i][j],
                                 right_side_max_map[i][j],
                                 up_side_max_map[i][j],
                                 down_side_max_map[i][j])
                if rain_level > heightMap[i][j]:
                    total_rain += rain_level - heightMap[i][j]
                    heightMap[i][j] = rain_level

        return total_rain

print(Solution().trapRainWater(heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))