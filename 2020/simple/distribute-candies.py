from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candies_set = set(candies)
        half_count = int(len(candies)/2)
        kind = len(candies_set)
        return kind if kind <= half_count else half_count

print(Solution().distributeCandies([1,1,1,3,3,3,4,4]))