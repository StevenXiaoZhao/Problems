class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A_len = len(A)
        for index in range(A_len):
            val = A[index]
            while val >0 and val < A_len and val != index +1 and A[val-1] != val:
                temp = A[val-1]
                A[val-1] = val
                A[index] = temp
                val = A[index]
        for index in range(A_len):
            if A[index] != index +1:
                return(index+1)
        return(A_len + 1)
            
ss = Solution()
test =  []
result = ss.firstMissingPositive(test)
print(result)