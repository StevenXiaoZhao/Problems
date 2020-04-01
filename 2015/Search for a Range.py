class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if(A == None):
            return([-1,-1])
        else:
            return(self.searchRangeInRange(A, target, 0, len(A)-1))
    
    def searchRangeInRange(self, A, target, start_index, end_index):
        if(start_index == end_index):
            if(target == A[start_index]):
                return([start_index,end_index])
            else:
                return([-1,-1])
        if(target < A[start_index] or target > A[end_index]):
            return([-1,-1])
        elif(target == A[start_index] and target == A[end_index]):
            return([start_index,end_index])
        elif(target == A[start_index]):
            for stop_index in range(start_index, end_index+1):
                if(A[stop_index] != target):
                    return([start_index,stop_index-1])
        elif(target == A[end_index]):
            for stop_index in range(start_index, end_index+1):
                if(A[stop_index] == target):
                    return([stop_index,end_index])
        else:
            mid_index = (start_index+end_index)//2
            [left_start, left_end] = self.searchRangeInRange(A, target, start_index, mid_index)
            [right_start, right_end] = self.searchRangeInRange(A, target, mid_index+1, end_index)
            if(left_end == -1):
                return([right_start, right_end])
            elif(right_start == -1):
                return([left_start, left_end])
            else:
                return([left_start, right_end])

ss = Solution()
testData = [5, 7, 7, 7, 8, 10]
result = ss.searchRange(testData, 6)
print(result)