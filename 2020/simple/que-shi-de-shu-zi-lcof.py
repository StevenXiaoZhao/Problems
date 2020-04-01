from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        i=0
        j=count-1
        if count-1 == nums[count-1]:
            return count

        while i<j:
            mid = int((i+j)/2)
            if nums[mid] == mid:
                i = mid + 1
            elif mid - 1>=0 and nums[mid-1] == mid-1:
                return mid
            else:
                j = mid - 1

        return i

print(Solution().missingNumber([0,1,2,3]))