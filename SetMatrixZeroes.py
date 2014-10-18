class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if(matrix == None):
            return(None)
        m = len(matrix)
        if(m==0):
            return(matrix)
        n = len(matrix[0])
        if(n == 0):
            return(matrix)
        exist_zero_first_line = False
        exist_zero_first_column = False
        for i in range(0, m):
            if(matrix[i][0] == 0):
                exist_zero_first_column = True
        for j in range(0, n):
            if(matrix[0][j] == 0):
                exist_zero_first_line = True
        for i in range(1, m):
            for j in range(1, n):
                if(matrix[i][j] == 0):
                    self.setPartZeros(matrix, i, j)
        for i in range(1,m):
            if(matrix[i][0] == 0):
                for j in range(1,n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if(matrix[0][j] ==0):
                for i in range(1,m):
                    matrix[i][j] = 0
        if(exist_zero_first_line == True):
            for j in range(0, n):
                matrix[0][j] = 0
        if(exist_zero_first_column == True):
            for i in range(0, m):
                matrix[i][0] = 0
    def setPartZeros(self, matrix, i, j):
        matrix[i][0] = 0
        matrix[0][j] = 0

a = [[1,1,1,1],[1,0,1,1],[1,1,1,1],[0,1,1,1]]
ss= Solution()
ss.setZeroes(a)
print(a)
        