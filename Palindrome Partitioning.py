class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        s_len = len(s)
        if s == '':
            return([[]])
        elif s_len == 1:
            return([[s]])
        result = []
        for i in range(1, s_len+1):
            curr = s[0:i]
            if(self.isPalindrome(curr) == False):
                continue
            if(i == s_len):
                result.append([curr]) 
                break
            subs = self.partition(s[i:s_len])
            for sub in subs:
                single = [curr]
                single.extend(sub)
                result.append(single)
        if result == []:
            result = [[]]
        return(result)
    def isPalindrome(self, string):
        string_len = len(string)
        s = 0
        e = string_len -1
        while(s<e):
            if(string[s] != string[e]):
                return(False)
            s +=1
            e -=1
        return(True)
ss = Solution()
result = ss.partition('aab')
print(result)
            