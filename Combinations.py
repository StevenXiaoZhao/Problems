class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if(k==1):
            result =[]
            for x in range(1,n+1):
                result.append([x])
            return(result)
        elif(n==k):
            result =[]
            for x in range(1,n+1):
                result.append(x)
            return([result])
        else:
            resultWithN = self.combine(n-1,k-1)
            for x in resultWithN:
                x.append(n)
            resultWithoutN = self.combine(n-1,k)
            resultWithN.extend(resultWithoutN)
            return(resultWithN)
ss= Solution()
result = ss.combine(10,5)
print(result)
            
            