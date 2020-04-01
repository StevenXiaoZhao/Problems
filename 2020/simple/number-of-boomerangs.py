from typing import List
import math


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        graph = dict()
        for point in points:
            graph[(point[0], point[1])] = dict()

        count = len(points)
        for i in range(count):
            for j in range(i + 1, count):
                distance = math.pow(points[i][0] - points[j][0], 2) + \
                           math.pow(points[i][1] - points[j][1], 2)
                dists = graph[(points[i][0], points[i][1])]
                distance=int(distance)
                if distance in dists:
                    dists[distance] += 1
                else:
                    dists[distance] = 1

                dists = graph[(points[j][0], points[j][1])]
                if distance in dists:
                    dists[distance] += 1
                else:
                    dists[distance] = 1

        count = 0
        for point in graph:
            dists = graph[point]
            for dist in dists:
                num = dists[dist]
                if num <= 1:
                    count += 0
                else:
                    count += num * (num - 1)

        return count

print(Solution().numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))
