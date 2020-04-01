from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if nums2 is None or n == 0:
            return nums1

        total_count = m + n
        while n > 0 and m > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[total_count - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[total_count - 1] = nums1[m - 1]
                m -= 1

            total_count -= 1

        while n > 0:
            nums1[total_count - 1] = nums2[n - 1]
            n -= 1
            total_count -= 1

t = [4, 5, 6, 0, 0, 0]
Solution().merge(t, 3, [1,2,3], 3)
print(t)
