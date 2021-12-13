from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stair_2 = 0
        stair_1 = 0

        for i in range(2, len(cost)+1):
            first_choice = cost[i-1] + stair_1
            second_choice = cost[i-2] + stair_2
            choice = first_choice if first_choice <= second_choice else second_choice
            stair_2 = stair_1
            stair_1 = choice

        return stair_1

print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


