class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        i=0
        c = x
        while(c>0):
            c = c//10
            i +=1
        return (self.isPalindromeBit(x,i))
        
        
    def isPalindromeBit(self, x, bit):
        if(x <0):
            return(False)
        elif(x<10 and bit <=1):
            return(True)
        else:
            right = x%10
            left = x//(10**(bit-1))
            if(left != right):
                return(False)
            else:
                return(self.isPalindromeBit((x-left*(10**(bit-1)))//10,bit-2))
ss= Solution()
a=10020001
result = ss.isPalindrome(a)
print(result)
                    