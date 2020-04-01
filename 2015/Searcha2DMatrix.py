class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if(m == 0):
            return False
        n = len(matrix[0])
        if(n ==0):
            return False
        elif(target < matrix[0][0] or target> matrix[m-1][n-1]):
            return False
        i= 0
        j=m-1
        mid=0
        while(True):
            mid = (i+j)//2
            if(i>=j):
                break
            if(matrix[mid][0] < target):
                i = mid
            if(matrix[mid][0] > target):
                j = mid -1
            
            if(matrix[j][0] <= target):
                mid = j
                break
            if(matrix[j][0] > target):
                j = j-1
            if(matrix[mid][0] == target):
                break
        i=0
        j=n-1
        while(True):
            mid2 = (i+j)//2
            if(i>j):
                return False
            elif(matrix[mid][mid2] == target):
                return True
            
            if(matrix[mid][mid2]>target):
                j=mid2 - 1
            if(matrix[mid][mid2]<target):
                i=mid2 + 1
ss= Solution()
a=[[1,2],[3,4]]
result = ss.searchMatrix(a,3)
print(result)
            
                