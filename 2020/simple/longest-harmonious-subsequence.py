from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                nums_dict[num] +=1
            else:
                nums_dict[num] =1
        max_pair = 0
        for key in nums_dict:
            if key+1 in nums_dict:
                pair = nums_dict[key] + nums_dict[key+1]
                if pair > max_pair:
                    max_pair = pair

        return max_pair

print(Solution().findLHS([1,3,2,2,5,2,3,7]))