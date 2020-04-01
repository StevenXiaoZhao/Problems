class Solution:
    # @return an integer
    def atoi(self, str):
        result = 0
        if(str == None):
            return(0)
        str_len = len(str)
        start = False
        positive = True
        for i in range(str_len):
            if('0'<=str[i] and str[i] <='9'):
                start = True
                result = result*10 + int(str[i])
                if(result>2147483647):
                    break
            elif(str[i] == '+'):
                if(start == False):
                    start = True
                else:
                    break
            elif(str[i] == '-'):
                if(start == False):
                    start = True
                    positive = False
                else:
                    break
            else:
                if(start == True):
                    break
                else:
                    if(str[i] != ' '):
                        break
                        
        if(result>2147483647):
            if(positive):
                result = 2147483647
            else:
                result = 2147483648
        if(positive  == False):
            result = - result
        return(result)
ss = Solution()
result = ss.atoi(' 11228552307  ')
print(result)
          