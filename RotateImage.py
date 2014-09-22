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
    			startVal = self.GetMatricsValue(matrix,x,y)
    			start_x = x
    			start_y = y
    			print(x)
    			print(y)
    			for x in range(1,5):
    				next_x = start_y
    				next_y = -start_x
    				next_val = self.GetMatricsValue(matrix,next_x,next_y)
    				self.SetMatricsValue(matrix,start_x,start_y,next_val)
    				self.SetMatricsValue(matrix,next_x,next_y, startVal)
    				startVal = next_val
    				start_x = next_x
    				start_y = next_y
    			y +=1
    		x+=1
    		print(x)
    		print(y)
    	return(matrix)


    def GetMatricsValue(self, matrix, x, y):
    	print('getValue: '+x)
    	print('getValue: '+y)
    	return(matrix[int(x + self.center)][int(y + self.center)])
    def SetMatricsValue(self, matrix, x, y,val):
    	matrix[int(x + self.center)][int(y + self.center)] = val

ss = Solution()

result = ss.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(result)
