class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        A_len = len(A)
        if(A_len <=2):
            return(0)
        
        b= [0]* A_len
        max_index = self.GetMax(A,0,A_len-1)
        left_max= A[0]
        for i in range(0, max_index):
            if(A[i] > left_max):
                left_max = A[i]
            b[i] = left_max
        right_max = A[A_len-1]
        for i in range(A_len-1, max_index, -1):
            if(A[i] > right_max):
                right_max = A[i]
            b[i] = right_max
        b[max_index] = A[max_index]
        result = 0
        for i in range(0, A_len):
            result += b[i] - A[i]
            
        return(result)

                
    def GetMax(self, A, i, j):
        max_val = A[i]
        max_index = i
        for x in range(i, j+1):
            if(A[x]>max_val):
                max_val = A[x]
                max_index = x
        return(max_index)
ss= Solution()
result = ss.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(result)
        
        