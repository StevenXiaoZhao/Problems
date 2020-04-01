class Solution:
    # @return an integer
    def romanToInt(self, s):
        transfer={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s_len = len(s)
        result = 0
        for x in range(0,s_len-1):
        	curr = transfer[s[x]]
        	next = transfer[s[x+1]]
        	if(curr>=next):
        		result += curr
        	else:
        		result -= curr
        result += transfer[s[s_len-1]]
        return(result)
ss= Solution()
result = ss.romanToInt('XCVII')
print(result)