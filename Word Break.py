class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if(s == '' or s == None):
            return(True)
        for word in dict:
            if s.startswith(word):
                sub = s.replace(word,'')
                result = self.wordBreak(sub,dict)
                if(result == True):
                    return(True)
        return(False)
ss = Solution()
print(ss.wordBreak('leetcode',["leetc", "code","lee","tcode"]))
        