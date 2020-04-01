from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price

            delta = price - min_price
            if delta> profit:
                profit = delta

        return profit

print(Solution().maxProfit([7,6,4,3,1]))