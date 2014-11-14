class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a_len = len(a)
        b_len = len(b)
        c_len = a_len + 1
        if(b_len > a_len):
            c_len = b_len +1
        c = ['0']*c_len
        while(a_len>0 or b_len >0):
            a_val = 0
            b_val = 0
            if(a_len >0):
                a_val = int(a[a_len-1])
            if(b_len >0):
                b_val = int(b[b_len-1])
            c_val = int(c[c_len-1])
            c_val +=a_val + b_val
            if(c_val <=1):
                c[c_len -1] = str(c_val)
            else:
                c[c_len -1] = str(c_val -2)
                c[c_len -2] = '1'
            a_len -=1
            b_len -=1
            c_len -=1
            
        if(c[0] == '0'):
            del(c[0])
        result =''
        for x in c:
            result +=x
        return(result)

ss= Solution()
result = ss.addBinary('11','1')
print(result)
            
        