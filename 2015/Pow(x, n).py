class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if(n == 0):
            return(1)
        elif(n == 1):
            return(x)
        else:
            isNegtive = False
            if(n<0):
                isNegtive = True
                n = -n
            half = n//2
            half_1 = self.pow(x,half)
            result = half_1*half_1
            if(n%2 !=0):
                result *= x
            if(isNegtive):
                result = 1/result
            return(result)
ss = Solution()
result = ss.pow(10,-5)
print(result)