class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        height = len(matrix)
        if height == 0:
            return([])
        width = len(matrix[0])
        leftIndex = 0
        rightIndex = width -1
        upIndex = 1
        downIndex = height -1
        direct = 'left'
        i = 0
        j = 0
        result = []
        while True:
            if len(result) >= width*height:
                break
            result.append(matrix[i][j])
            if direct == 'left':
                if j< rightIndex:
                    j +=1
                else:
                    rightIndex -=1
                    direct = 'down'
                    i +=1
            elif direct == 'down':
                if i< downIndex:
                    i +=1
                else:
                    downIndex -=1
                    direct = 'right'
                    j -=1
            elif direct == 'right':
                if j > leftIndex:
                    j -=1
                else:
                    leftIndex +=1
                    direct = 'up'
                    i -=1
            elif direct == 'up':
                if i > upIndex:
                    i -=1
                else:
                    upIndex +=1
                    direct = 'left'
                    j +=1 
        return(result)

ss= Solution()
test = [[2,5,8],[4,0,-1]]
result = ss.spiralOrder(test)
print(result)