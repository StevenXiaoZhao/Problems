from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        position = dict()
        count_nums2 = len(nums2)
        for i in range(count_nums2):
            position[nums2[i]] = i

        count_nums1 = len(nums1)
        for i in range(count_nums1):
            j = position[nums1[i]] + 1
            found = False
            while j < count_nums2:
                if nums2[j] > nums1[i]:
                    nums1[i] = nums2[j]
                    found = True
                    break
                j+=1

            if not found:
                nums1[i] = -1

        return nums1

print(Solution().nextGreaterElement([2,4],[1,2,3,4]))
