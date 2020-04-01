from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        t = nums.copy()
        t.sort(reverse=True)
        p = dict()
        i = 1
        for num in t:
            p[num] = i
            i += 1
        result = []
        for num in nums:
            if p[num] == 1:
                result.append("Gold Medal")
            elif p[num] == 2:
                result.append("Silver Medal")
            elif p[num] == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(p[num]))

        return result

print(Solution().findRelativeRanks([3, 2, 1,5, 4, ]))