class Solution:
    # @return an integer
    def numTrees(self, n):
        c= [1,1] + [0]*(n-1)
        for i in range(2, n+1):
            for j in range(i):
                c[i] += c[j]*c[i-1-j]
        return(c[n])
ss = Solution()
result = ss.numTrees(3)
print(result)