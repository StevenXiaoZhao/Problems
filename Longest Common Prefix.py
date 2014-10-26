class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        strCount = len(strs)
        if(strCount == 0):
            return('')
        elif(strCount == 1):
            return(strs[0])
        strMinLen = len(strs[0])
        for x in range(0, strCount):
            if(strMinLen > len(strs[x])):
                strMinLen = len(strs[x])
        i=0
        while(True):
            same = True
            if(i>strMinLen -1):
                break
            val = strs[0][i]
            for x in range(0, strCount):
                if(val != strs[x][i]):
                    same = False
                    break
            if(same == False):
                break
            i+=1
        return strs[0][0:i]
ss= Solution()
testData =['1123','','1']
result = ss.longestCommonPrefix(testData)
print(result)