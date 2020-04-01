from typing import List
import math


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        prev_zero_index = -1
        dist = 0
        zero_time = False
        for i in range(len(seats)):
            if seats[i] == 0:
                if not zero_time:
                    prev_zero_index = i
                    zero_time = True

                if i == len(seats)-1 and zero_time:
                    count = i - prev_zero_index + 1
                    if count > dist:
                        dist = count
            else:
                if zero_time:
                    count = i-prev_zero_index
                    if prev_zero_index !=0:
                        count = math.ceil(count/2)
                    if count > dist:
                        dist = count
                    zero_time = False
        return dist

print(Solution().maxDistToClosest([0,0]))
