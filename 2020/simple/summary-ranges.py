from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        result = []
        start = nums[0]
        curr = start
        for i in range(1, len(nums)):
            num = nums[i]
            if num == curr + 1:
                curr += 1
            elif start == curr:
                result.append(str(start))
                start = num
                curr = num
            else:
                result.append(str(start) + "->" + str(curr))
                start = num
                curr = num

        if start == curr:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(curr))

        return result

print(Solution().summaryRanges([0,1,2,4,5,7]))
