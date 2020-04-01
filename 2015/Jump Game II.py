class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        A_len = len(A)
        maxReached = A[0]
        edge = 0
        step = 0
        for i in range(0, A_len):
            if(i>edge):
                step +=1
                edge = maxReached
            
            if(edge>=A_len-1):
                return(step)
            currReach = A[i] + i
            if(currReach > maxReached):
                maxReached = currReach
            if(maxReached == i):
                return(-1)

        return(step)
ss = Solution()
result = ss.jump([10])
print(result)