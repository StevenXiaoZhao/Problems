from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums)
        while start_index <= end_index:
            mid_index = int((start_index + end_index) / 2)
            if nums[mid_index] == target:
                return mid_index
            elif target > nums[mid_index]:
                if mid_index+1 >= len(nums):
                    return len(nums)
                elif target < nums[mid_index+1]:
                    return mid_index+1
                else:
                    start_index = mid_index + 1
            else:
                if mid_index-1 < 0:
                    return 0
                elif target > nums[mid_index-1]:
                    return mid_index
                else:
                    end_index = mid_index - 1

        return len(nums)

print(Solution().searchInsert([1, 3, 5, 6], 0))
