class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    center = 0
    def rotate(self, matrix):
    	matrix_len = len(matrix)

    	if(matrix_len <=1):
    		return(matrix)
    	self.center = (matrix_len-1)/2
    	x = self.center%1
    	while(x<= self.center):
    		y = self.center%1
    		while(y<=self.center):
    			startVal = (matrix[int(x + self.center)][int(y + self.center)])
    			start_x = x
    			start_y = y
    			for i in range(1,5):
    				next_x = start_y
    				next_y = -start_x
    				next_val = matrix[int(next_x + self.center)][int(next_y + self.center)] 
    				matrix[int(next_x + self.center)][int(next_y + self.center)] = startVal
    				startVal = next_val
    				start_x = next_x
    				start_y = next_y
    			y +=1
    		x+=1
    	return(matrix)

ss = Solution()
a= [[1,2],[3,4]] 
result = ss.rotate(a)
print(a)
