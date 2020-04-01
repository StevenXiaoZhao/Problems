from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_place = 0
        count = len(flowerbed)
        if count == 0:
            return n == 0
        if count == 1:
            return flowerbed[0] + n < 2

        if flowerbed[1] == 0 and flowerbed[0] == 0:
            max_place += 1
            flowerbed[0] = 1

        for i in range(1, count - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                max_place += 1
                i += 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            max_place += 1


        return n <= max_place


print(Solution().canPlaceFlowers(flowerbed=[0, 0,0,0, 1], n=2))
