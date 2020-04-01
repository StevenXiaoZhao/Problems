class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if(obstacleGrid[0][0] ==1):
            return(0)
        else:
            obstacleGrid[0][0] = -1
            rows = len(obstacleGrid)
            columns = len(obstacleGrid[0])
            if(obstacleGrid[rows-1][columns-1] ==1):
                return(0)
            for i in range(0, rows):
                for j in range(0, columns):
                    if(i==0 and j==i):
                        obstacleGrid[0][0] = -1
                    else:
                        if(obstacleGrid[i][j] == 1):
                            continue
                        elif(i==0):
                            if(obstacleGrid[i][j-1]!=1):
                                obstacleGrid[i][j] = obstacleGrid[i][j-1]
                        elif(j==0):
                            if(obstacleGrid[i-1][j]!=1):
                                obstacleGrid[i][j] = obstacleGrid[i-1][j]
                        else:
                            if(obstacleGrid[i-1][j] !=1):
                                obstacleGrid[i][j] +=obstacleGrid[i-1][j]
                            if(obstacleGrid[i][j-1] !=1):
                                obstacleGrid[i][j] +=obstacleGrid[i][j-1]
            return(-obstacleGrid[rows-1][columns-1])
testData = [[0,0,0],[0,1,0],[0,1,0]]
ss=Solution()
result = ss.uniquePathsWithObstacles(testData)
print(result)