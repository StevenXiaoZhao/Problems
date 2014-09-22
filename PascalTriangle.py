class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
    	if(numRows <=0):
    		return([])
    	elif(numRows ==1):
    		return([[1]])
    	a=[1]
    	result=[]
    	result.append(a)
    	row =[]
    	i=1
    	for x in range(1,numRows):
        	row = [1]
        	a_len = len(a)
        	for i in range(1,a_len):
        		row.extend([a[i]+a[i-1]])
        	row.extend([1])
        	result.append(row)
        	a = row
    	return(result)
ss= Solution()






result = ss.generate(2)
print(result)
        		