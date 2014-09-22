class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a1=1
        a2=2
        if(n<=0):
        	return 0
        elif(n==1):
        	return 1
        elif(n==2):
        	return 2
        else:
        	a_i=1
        	a_i1=2
        	result =0
        	for x in range(3,n+1):
        		result = a_i +a_i1
        		a_i = a_i1
        		a_i1 = result
        	return result
ss= Solution()
result = ss.climbStairs(5)
print(result)
