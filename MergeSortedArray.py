class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
    	lastIndex_A = m-1
    	lastIndex_B = n-1
    	lastIndex_total = m+n-1
    	while(lastIndex_A>=0 and lastIndex_B>=0) :
    		if(A[lastIndex_A]>B[lastIndex_B]):
    			A[lastIndex_total] = A[lastIndex_A]
    			lastIndex_A -=1
    		else:
    			A[lastIndex_total] = B[lastIndex_B]
    			lastIndex_B -=1
    		lastIndex_total -=1
    	if(lastIndex_B>=0):
    		for x in range(0,lastIndex_B+1):
    			A[x] = B[x]


ss = Solution()
a=[0,1,2,3,4,0,0,0,0]
ss.merge(a,5,[-1,4,6,8],4)
print(a)