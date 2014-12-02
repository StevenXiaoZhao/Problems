class Solution:
    # @return a string
    def convert(self, s, nRows):
        ss = ['']*nRows
        i =0
        add = True
        for x in s:
            ss[i] = ss[i] + x
            if(add):
                if(i<nRows -1):
                    i+=1
                else:
                    i -=1
                    add = False
            else:
                if(i>0):
                    i-=1
                else:
                    i +=1
                    add = True
        result = ''
        for s_s in ss:
            result += s_s
        return(result)
ss = Solution()
result = ss.convert("PAYPALISHIRING", 1)
print(result)