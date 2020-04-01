class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        if len(nums1)<len(nums2):
            nums1 = nums1 + ['0']*(len(nums2)-len(nums1))
        elif len(nums1)>len(nums2):
            nums2 = nums2 + ['0']*(len(nums1)-len(nums2))
            
        num_len = len(nums1)
        for i in range(num_len):
            if int(nums1[i]) > int(nums2[i]):
                return(1)
            elif int(nums1[i]) < int(nums2[i]):
                return(-1)
        return(0)
ss = Solution()
result = ss.compareVersion('13.0','13')
print(result)

