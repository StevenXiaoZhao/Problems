from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if nums is None or len(nums) ==0:
            return 0

        # compute degree
        num_count = dict()
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        degree = max(num_count.values())

        if degree == 1:
            return 1

        count = len(nums)
        shortest_sub = count
        num_begin_index = dict()
        num_curr_count = dict()

        for i in range(count):
            if num_count[nums[i]] == degree:
                if nums[i] not in num_begin_index:
                    num_begin_index[nums[i]] = i
                    num_curr_count[nums[i]] = 1
                else:
                    num_curr_count[nums[i]] += 1

                if num_curr_count[nums[i]] == degree:
                    length = i + 1 - num_begin_index[nums[i]]
                    if length < shortest_sub:
                        shortest_sub = length

        return shortest_sub


print(Solution().findShortestSubArray([1,2,3,4,5,6]))
