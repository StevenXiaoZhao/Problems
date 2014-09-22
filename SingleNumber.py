class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        a_len = len(A)
        if(a_len ==0):
        	return(0)
        if(a_len ==1):
        	return(A[0])
        for x in range(1,a_len):
        	A[0]=A[0]^A[x]
        return(A[0])

s = Solution()
p = s.singleNumber([1,1,3])
print(p)