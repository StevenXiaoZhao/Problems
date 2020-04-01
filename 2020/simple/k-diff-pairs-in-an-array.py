from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0 or k < 0:
            return 0
        count = 0

        if k == 0:
            nums_dict = dict()
            for num in nums:
                if num in nums_dict:
                    nums_dict[num] += 1
                else:
                    nums_dict[num] = 1

            for num in nums_dict:
                if nums_dict[num] > 1:
                    count += 1
        else:
            nums_set = set(nums)
            for num in nums_set:
                if num + k in nums_set:
                    count += 1

        return count


print(Solution().findPairs([1, 3, 1, 5, 4, 1, 1, 3], k=0))
