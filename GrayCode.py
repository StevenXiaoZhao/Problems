class Solution:
    # @return a list of integers
    def grayCode(self, n):
    	max=2^n
    	result = [0]*n
    	for x in range(1,max):
    		for i in range(0,n+1):
    			if(x%(2^(i+1)) == 2^i):
