class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        val = 1
        max= n**2
        i=0
        j=0
        direction = 'forward'
        matrix  = [[0 for col in range(n)] for row in range(n)] 
        for val in range(1, max+1):
            matrix[i][j] = val
            [i,j,direction] = self.GetNextPosition(matrix,i,j,n,direction)
        return(matrix)
    def GetNextPosition(self, matrix, i,j,n,direction):
        if(direction == 'forward'):
            if(j<n-1 and matrix[i][j+1] == 0):
                return ([i,j+1,direction])
            else:
                return ([i+1,j, 'down'])
        elif(direction == 'down'):
            if(i<n-1 and matrix[i+1][j] == 0):
                return ([i+1,j,direction])
            else:
                return ([i,j-1,'backward'])
        elif(direction == 'backward'):
            if(j>0 and matrix[i][j-1] == 0):
                return ([i,j-1,direction])
            else:
                return ([i-1,j,'up'])
        elif(direction == 'up'):
            if(i>0 and matrix[i-1][j] == 0):
                return ([i-1,j,direction])
            else:
                return ([i,j+1,'forward'])
         
ss = Solution()
result = ss.generateMatrix(4)
print(result)