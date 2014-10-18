class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        if(m==0):
            return(0)
        n=len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if(i==0 and j ==0):
                    continue
                if(i>0 and j ==0):
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif(j>0 and i ==0):
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        return(grid[m-1][n-1])

ss = Solution()

a=[[1,2,7],[3,0,4],[2,1,5]]
b=[[1,2],[1,1]]

result = ss.minPathSum(b)

print(result)
        