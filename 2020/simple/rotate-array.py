from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        if nums is None:
            return None

        count = len(nums)

        if count <= 1 or k==0:
            return None

        val = nums[0]
        start = 0
        j = 0
        for i in range(count):

            replace_index = (j+k)%count
            val1 = nums[replace_index]
            nums[replace_index] = val
            val = val1
            j=replace_index

            if j == start:
                j=(j+1)%count
                val = nums[j]
                start = j

t = [1,2]
Solution().rotate(t,2)
print(t)