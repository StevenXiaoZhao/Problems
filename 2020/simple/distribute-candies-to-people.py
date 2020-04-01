from typing import List
import math

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        once_max_candie = int(math.sqrt(2*candies+0.25)-0.5) # 最后一个一次性发的最大数目的糖果
        left_candies_count = int(candies-(once_max_candie+1)*once_max_candie/2) # 最大数目发完以后，还剩下的糖果
        full_circle = int(once_max_candie/num_people) # 完完整整可以发几轮
        last_circle_once_max_candie_index = once_max_candie - full_circle*num_people -1
        distribute = [0]*num_people # 记录分发情况
        for i in range(num_people):
            circle_count = full_circle
            if i<= last_circle_once_max_candie_index:
                circle_count += 1

            if circle_count == 0:
                break

            distribute[i] = int(circle_count*(i+1) + (circle_count-1)*circle_count*num_people/2)
        distribute[(last_circle_once_max_candie_index+1)%num_people]+=left_candies_count

        return distribute

print(Solution().distributeCandies(candies = 10, num_people = 20))

