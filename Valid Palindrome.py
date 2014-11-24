class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s_len = len(s)
        s = s.upper()
        i = 0
        j = s_len -1
        while(i<=j):
            if(s[i].isalnum() == False):
                i+=1
            elif(s[j].isalnum() == False):
                j-=1
            else:
                if(s[i] == s[j]):
                    i+=1
                    j-=1
                else:
                    return(False)
        return(True)
s="A man, a plan, a canal: Panama"
ss = Solution()
result = ss.isPalindrome('1a2')
print(result)