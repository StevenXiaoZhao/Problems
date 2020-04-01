class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        A_len = len(A)
        if(A_len == 0):
            return(False)
        else:
            return (self.searchIndex(A, target, 0, A_len -1))
    
    
    def searchIndex(self, A, target, i, j):
        
        if(i==j or j-i == 1):
            if(A[i] == target or A[j] == target):
                return(True)
            else:
                return(False)
        elif(A[i]<A[j]):
            if(target <A[i] or target >A[j]):
                return(False)
            else:
                mid = (i+j)//2
                if(A[mid]==target):
                    return(True)
                elif(A[mid] < target):
                    return(self.searchIndex(A, target,mid+1,j))
                else:
                    return(self.searchIndex(A, target,i,mid-1))
        else:
            mid = (i+j)//2
            if(A[mid] == target):
                return(True)
            else:
                left = self.searchIndex(A, target,i,mid-1)
                if(left != False):
                    return(True)
                else:
                    return(self.searchIndex(A, target,mid+1,j))
ss = Solution()

result = ss.search([1,1,3],1)
print(result)