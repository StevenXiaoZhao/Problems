from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r <= 0 or c <= 0 or nums is None:
            return nums
        row_count = len(nums)
        col_count = 0 if row_count == 0 else len(nums[0])
        if r * c != row_count * col_count:
            return nums

        new_nums = []

        if r ==1:
            for num_arr in nums:
                for num in num_arr:
                    new_nums.append(num)

            return [new_nums]

        i = 0
        new_row = []

        for num_arr in nums:
            for num in num_arr:
                new_row.append(num)
                i += 1
                if i == c:
                    new_nums.append(new_row)
                    new_row = []
                    i=0
        return new_nums

print(Solution().matrixReshape([[1, 2, 5, 3, 4, 6]],  6,1))