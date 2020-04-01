class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        A_len = len(A)
        if(A_len == 0):
            return(-1)
        else:
            return (self.searchIndex(A, target, 0, A_len -1))
    
    
    def searchIndex(self, A, target, i, j):
        
        if(i==j or j-i == 1):
            if(A[i] == target):
                return(i)
            elif(A[j] == target):
                return(j)
            else:
                return(-1)
        elif(A[i]<A[j]):
            if(target <A[i] or target >A[j]):
                return(-1)
            else:
                mid = (i+j)//2
                if(A[mid]==target):
                    return(mid)
                elif(A[mid] < target):
                    return(self.searchIndex(A, target,mid+1,j))
                else:
                    return(self.searchIndex(A, target,i,mid-1))
        else:
            mid = (i+j)//2
            if(A[mid] == target):
                return(mid)
            else:
                left = self.searchIndex(A, target,i,mid-1)
                if(left != -1):
                    return(left)
                else:
                    return(self.searchIndex(A, target,mid+1,j))
ss = Solution()

result = ss.search([3,1],0)
print(result)