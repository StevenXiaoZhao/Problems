class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        A_len = len(A)
        for x in range(1,A_len):
        	if(A[x-1]>0):
        		A[x] = A[x-1]+A[x]
        return max(A)

ss= Solution()
print(ss.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))