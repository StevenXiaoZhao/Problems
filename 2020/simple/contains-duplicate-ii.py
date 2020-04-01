from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if nums is None or len(nums) == 0 or k==0:
            return False

        count = len(nums)
        if count <= k:
            duplicate = set(nums)
            return len(duplicate) != count

        duplicate = set(nums[0:k])
        for i in range(k, count):
            if nums[i] in duplicate:
                return True

            duplicate.remove(nums[i-k])
            duplicate.add(nums[i])

        return False

tt= [1,2,1]
a=0

print(Solution().containsNearbyDuplicate(nums = tt, k = a))