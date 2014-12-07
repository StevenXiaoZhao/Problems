class Solution:
    # note:
    # we need to know that condition: num[-1] = num[n] = -¡Ş.
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        num_len = len(num)
        if(num_len <=1):
            return(0)
        else:
            s= 0
            e= num_len -1
            while(s<e):
                mid = (s+e)//2
                if(num[mid+1]>num[mid]):
                    s = mid+1
                elif(num[mid-1] > num[mid]):
                    e = mid-1
                else:
                    return(mid)
            return(s)
ss = Solution()
result = ss.findPeakElement([1, 2, 3, 1])
print(result)