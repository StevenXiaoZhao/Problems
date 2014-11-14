class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        
        return(result)
    
    def generateParenthesisArray(self, n):
        if(n == 1):
            return([['(',')']])
        else:
            subParenthesis = self.generateParenthesisArray(n-1)
            for Parenthesis in subsubParenthesis:
                
    def ToString(self, strArray):
        result =''
        for x in strArray:
            result +=x
        return(result)
ss= Solution()
result = ss.generateParenthesis(3)
print(result)
                
        