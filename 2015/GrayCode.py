class Solution:
    # @return a list of integers
    def grayCode(self, n):
        maxTimes=2**n
        result = [0]*n
        numSeq = [0]*maxTimes
        for x in range(1,maxTimes):
            isChanged = False
            for i in range(0,n):
                if(x == 2**i): #start change position
                    result[i] = 1- result[i]
                    isChanged = True
                    break
                elif( (x - 2**i)%(2**(i+1)) == 0): #circle to change
                    result[i] = 1- result[i]
                    isChanged = True
                    break
            if(isChanged):
                num = 0
                for i in range(n):
                    num += result[i]*(2**i)
                numSeq[x] = num
            else:
                maxTimes = x
                break
        return numSeq[0:maxTimes]
ss = Solution()
result = ss.grayCode(5)
print(result)
