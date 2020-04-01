class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s_len = len(s)
        meetWord = -1
        for i in range(s_len -1, -1, -1):
            if(s[i] != ' ' and meetWord < 0):
                meetWord = i
            elif(s[i] == ' ' and meetWord > 0):
                return(meetWord - i)
        return(meetWord +1)
ss = Solution()
s="hhjknbjh  "
result = ss.lengthOfLastWord(s)
print(result)
        
        
        