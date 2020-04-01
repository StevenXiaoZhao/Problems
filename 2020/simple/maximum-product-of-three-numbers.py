from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        min_arr = nums[0:2]
        for num in nums[2:]:
            min_arr.sort()
            if num < min_arr[1]:
                min_arr[1] = num

        min_arr.sort()

        max_arr = nums[0:3]
        for num in nums[3:]:
            max_arr.sort()
            if num > max_arr[0]:
                max_arr[0] = num

        max_arr.sort()

        temp = max_arr[0] * max_arr[1]
        if min_arr[0] < 0 and min_arr[1] < 0:
            temp1 = min_arr[0] * min_arr[1]
            if temp1 > temp:
                temp = temp1

        return temp * max_arr[2]


print(Solution().maximumProduct([1, 2, 3, 4, 10,20,-10,-8]))
