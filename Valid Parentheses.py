class Solution:
    # @return a boolean
    def isValid(self, s):
        s_len = len(s)
        stack = []
        for i in range(0, s_len):
            c = s[i]
            if(self.isParenthese(c)):
                if(self.isLeftParenthese(c)):
                    stack.append(c)
                elif(self.isRightParenthese(c)):
                    if(len(stack)<=0):
                        return(False)
                    else:
                        if(self.isMatchedParenthese(stack.pop(),c) == False):
                            return(False)
        if(len(stack) == 0):
            return(True)
        else:
            return(False)
                       
                    
                
                
    def isParenthese(self, c):
        return c == '(' or c == ')' or c == '[' or c == ']' or c =='{' or c == '}'
    def isLeftParenthese(self, c):
        return c == '(' or c == '[' or c =='{'
    def isRightParenthese(self, c):
        return c == ')' or c == ']' or c =='}'
    def isMatchedParenthese(self, left, right):
        return left == '(' and right == ')' or left == '[' and right == ']' or left =='{' and right == '}'    
ss = Solution()
s='(()[]{}))'
result = ss.isValid(s)
print(result)