class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = ''
        while num > 0:
            currNum = num % 26
            if currNum == 0:
                currNum = 26
            currChar = chr(currNum+64)
            result = currChar + result
            if currNum == num:
                break
            num = (num - currNum)//26
        return(result)
ss = Solution()
result = ss.convertToTitle(55)
print(result)