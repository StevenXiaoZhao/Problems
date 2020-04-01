class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
    	A_len = len(A)
    	i=0
    	while(True):
    		if(i>A_len-1):
    			break
    		else:
    			a = A[i]
    			if(a == elem):
    				A.remove(a)
    				A_len = len(A)
    			else:
    				i = i+1
    	return(len(A))

ss= Solution()
print(ss.removeElement([4,4], 4))