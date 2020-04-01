class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        A_len = len(A)
        return self.search(A,target, 0, A_len-1)


    def search(self, A, target, start, end):
        if(A[start]>=target):
        	return start
        elif(A[end] == target):
        	return end
        elif(A[end] < target):
        	return end + 1
        elif(start == end):
        	return start
        elif(end - start ==1):
        	return start +1
        else:
        	mid = (start + end)//2
        	if(target <= A[mid]):
        		return self.search(A, target, start, mid)
        	else:
        		return self.search(A, target, mid+1, end)

a=[3,5,7,9,10]
ss = Solution()
result = ss.searchInsert(a,8)
print(result)