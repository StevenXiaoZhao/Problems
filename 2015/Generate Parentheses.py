class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = self.generateParenthesisArray(n,n)
        return(result)
    
    def generateParenthesisArray(self, left, right):
        if(left == 0):
            return([')'*right])
        else:
            result = []
            curr = ''
            if(left == right): # only left can generated
                curr='('
                subSeq = self.generateParenthesisArray(left-1,right)
                for sub in subSeq:
                    result.append(curr+sub)
            else: #must be left > right, two choice
                curr = '('
                subSeq = self.generateParenthesisArray(left-1,right)
                for sub in subSeq:
                    result.append(curr+sub)
                curr = ')'
                subSeq = self.generateParenthesisArray(left,right-1)
                for sub in subSeq:
                    result.append(curr+sub)
            return(result)
                
    def ToString(self, strArray):
        result =''
        for x in strArray:
            result +=x
        return(result)
ss= Solution()
result = ss.generateParenthesis(3)
print(result)
                
        