class Solution:
    # @return an integer
    def reverse(self, x):
        result =0
        isNeg =False
        if(x<0):
        	isNeg = True
        	x = -x
        while(True):
        	c=x%10
        	result = result*10 + c
        	x=x//10
        	if(x==0):
        		break
        if(isNeg):
        	result = -result
        return(result)

ss= Solution()
s= ss.reverse(-1234)
print(s)