class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        maxProduct = -1000000
        currProduct = 1
        if( A == None or A == []):
            return(None)
        else:
            startIndex = 0
            endIndex = -1
            for x in A:
                if(x == 0):
                    if(maxProduct<0):
                        maxProduct = 0
                    result = self.maxProductWithout0(A, startIndex, endIndex)
                    if(result>maxProduct):
                        maxProduct = result
                    endIndex +=1
                    startIndex = endIndex+1
                    
                else:
                    endIndex +=1
            if(startIndex < len(A) and endIndex < len(A)):
                result = self.maxProductWithout0(A, startIndex, endIndex)
                if(result>maxProduct):
                    maxProduct = result
        return(maxProduct)
    def maxProductWithout0(self, A, startIndex, endIndex):
        negCount = 0
        product = 1
        firstNegIndex = -1
        firstNegProduct = -1
        lastNegIndex = -1
        lastNegProduct = -1
        if(startIndex > endIndex):
            return(0)
        elif(startIndex == endIndex):
            return(A[startIndex])
        else:
            for x in range(startIndex, endIndex+1):
                product *= A[x]
                if(A[x] <0):
                    negCount +=1
                    lastNegIndex = x
                    lastNegProduct = product
                    if(firstNegIndex == -1):
                        firstNegIndex = x
                        firstNegProduct = product
            if negCount%2 == 0:
                return(product)
            else:
                right = product//firstNegProduct
                left = lastNegProduct//A[lastNegIndex]
                if(left > right):
                    return(left)
                return(right)
            
        
        
        
ss = Solution()
result = ss.maxProduct([-6,0,-7])
print(result)