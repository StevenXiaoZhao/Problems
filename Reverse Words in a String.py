class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        a=[]
        word = ''
        if( s == None):
            return(None)
        for x in s:
            if(x == ' '):
                if word == '':
                    continue
                else:
                    a.insert(0, word)
                    word = ''
            else:
                word += x
        if(word != ''):
            a.insert(0, word)
        reversedStr = ''
        for x in a:
            if(reversedStr != ''):
                reversedStr = reversedStr + ' '
            reversedStr = reversedStr + x
        return(reversedStr)

ss = Solution()
result = ss.reverseWords(' the sky        is blue ')
print(result)