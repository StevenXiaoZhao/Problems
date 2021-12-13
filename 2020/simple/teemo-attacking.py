from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        max_time = -1
        period = 0
        for attack in timeSeries:
            if attack > max_time:
                new_period = duration
                max_time = attack + duration - 1
            else:
                new_period = attack + duration - 1 - max_time
                max_time += new_period

            if new_period > 0:
                period += new_period

        return period

#print(Solution().findPoisonedDuration([0,1,2,4],2))
print(Solution().findPoisonedDuration([0,1,2,4],3))
