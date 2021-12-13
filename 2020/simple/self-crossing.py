from typing import List


class Solution:

    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        if n < 4:
            return False

        i = 2
        while i< n and distance[i] > distance[i - 2]:
            i += 1

        if i == n:
            return False

        if distance[i] >= distance[i - 2] - (0 if i < 4 else distance[i - 4]):
            distance[i - 1] -= 0 if i < 3 else distance[i - 3]

        i+=1
        while i <n and distance[i] < distance[i - 2]:
            i += 1

        return i != n


print(Solution().isSelfCrossing(
    distance=[3,3,3,2,1,1]))
