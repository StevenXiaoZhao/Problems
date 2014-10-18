class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        A_len = len(A)
        if(A_len <= 2):
            return(A_len)
        start_index = 0
        miner = A[0]-1
        for consider_index in range(1,A_len):
            if(A[consider_index] == A[start_index]):
                if(consider_index - start_index ==1):
                    continue
                else:
                    A[consider_index] = miner
            else:
                start_index = consider_index
        start_index = 2
        consider_index = 2
        while(start_index<A_len and consider_index < A_len):
            if(A[consider_index] == miner or consider_index <= start_index):
                consider_index +=1
                continue            
            if(A[start_index] != miner):
                start_index +=1
                continue
            A[start_index] = A[consider_index]
            A[consider_index] = miner
        while(start_index < A_len and A[start_index] != miner):
            start_index +=1
            
        return(start_index)

ss= Solution()
a=[1]
result = ss.removeDuplicates(a)
print(result)
print(a)
            