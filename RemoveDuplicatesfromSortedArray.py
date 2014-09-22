class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        A_len = len(A)
        if(A_len <=1):
        	return(A_len)
        unique_i = 1
        for i in range(1,A_len):
        	if(A[i] != A[i-1]):
        		A[unique_i] = A[i]
        		unique_i +=1
        return(unique_i)

ss= Solution()

p = []
q=ss.removeDuplicates(p)
print(q)