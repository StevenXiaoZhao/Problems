class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        A_len = len(A)
        max_reach = 0
        for i in range(0, A_len):
            if(i == A_len -1):
                return(True)
            elif(A[i] == 0):
                if(max_reach <= i):
                    return(False)
            else:
                if(i+A[i]>max_reach):
                    max_reach = i+A[i]
        
testData = [2,0]
ss= Solution()
result = ss.canJump(testData)
print(result)