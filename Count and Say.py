class Solution:
    # @return a string
    def countAndSay(self, n):
        s1 = '1'
        s2 = ''
        for i in range(0, n-1):
            c=s1[0]
            count = 0
            s2 = ''
            for x in s1:
                if(c == x):
                    count+=1
                else:
                    s2 += str(count)+c
                    count = 1
                    c = x
            s2 += str(count)+c
            s1 = s2
        return(s1)

ss = Solution()
test =5
result = ss.countAndSay(test)
print(result)