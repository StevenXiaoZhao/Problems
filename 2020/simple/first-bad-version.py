# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >=1702766719


class Solution:
    def firstBadVersion(self, n):
        return self.findFirstBadVersion(1, n)

    def findFirstBadVersion(self, s:int, e:int)->int:
        while e>=s:
            mid = int((s+e)/2)
            if isBadVersion(mid):
                if mid ==1 or not isBadVersion(mid-1):
                    return mid
                e=mid-1
            else:
                s=mid+1

            print(str(s)+':' +str(e))
print(Solution().firstBadVersion(2702766719))
