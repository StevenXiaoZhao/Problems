from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None or nums2 is None:
            return []

        if len(nums1) > len(nums2):
            check = set(nums2)
            nums = nums1
        else:
            check = set(nums1)
            nums = nums2

        result = set()
        for num in nums:
            if num in check:
                result.add(num)

        return list(result)

print(Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2]))