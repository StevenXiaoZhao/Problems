class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        return(self.GetIpGroups(s,4))
        
    def GetIpGroups(self, s, num):
        if s == '':
            return([])
        if num == 1:
            if s[0] == '0' and len(s) >1:
                return([])
            integer = int(s)
            if integer <= 255:
                return([s])
            else:
                return([])
        else:
            result = []
            for i in range(len(s)-1):
                char = s[0:i+1]
                leftStr = s[i+1:len(s)]
                if len(leftStr) > (num -1)*3:
                    continue
                elif len(leftStr) <num -1:
                    break
                elif char[0] == '0' and len(char) >1:
                    break
                curr = int(char)
                if curr > 255:
                    break
                else:
                    lefts = self.GetIpGroups(leftStr, num -1)
                    if lefts == []:
                        continue
                    for left in lefts:
                        new = char + '.' + left
                        result.append(new)
            return(result)
ss = Solution()
result = ss.restoreIpAddresses("10010010256")
print(result)