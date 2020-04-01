class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
    	grid = [([0] * n) for i in range(m)]
    	grid[0]=1
    	for x in range(0,m):
    		grid[x][0] =1
    	for x in range(1,m):
    		for i in range(1,n):
    			grid[x][i] = grid[x-1][i] + grid[x][i-1]
    	return(grid[m-1][n-1])

ss= Solution()
result = ss.uniquePaths(4,4)

        