class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        rows_num = len(triangle)
        for i in range(rows_num-2, -1, -1):
            row_len = len(triangle[i])
            for j in range(0, row_len):
                smaller = triangle[i+1][j]
                if(smaller > triangle[i+1][j+1]):
                    smaller = triangle[i+1][j+1]
                triangle[i][j] +=smaller
        return(triangle[0][0])
ss = Solution()
testData = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

result = ss.minimumTotal(testData)
print(result)