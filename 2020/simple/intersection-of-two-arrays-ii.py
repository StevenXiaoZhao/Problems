from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None or nums2 is None:
            return []

        nums1_dict = self.list2dict(nums1)
        nums2_dict = self.list2dict(nums2)
        result = []
        for num in nums1_dict:
            if num in nums2_dict:
                count = nums1_dict[num] if nums1_dict[num] <= nums2_dict[num] else nums2_dict[num]
                result.extend([num]*count)

        return result

    def list2dict(self, nums:List[int])->dict:
        nums_dict = dict()
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] =1
            else:
                nums_dict[num] +=1

        return nums_dict

print(Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))