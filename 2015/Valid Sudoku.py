class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    number = ['1','2','3','4','5','6','7','8','9']
    def isValidSudoku(self, board):
        count={}
        board_len = len(board)
        for i in range(0, board_len):
            self.resetCount(count)
            for j in range(0, board_len):
                if(board[i][j] != '.'):
                    count[board[i][j]] +=1
                    if(count[board[i][j]]>1):
                        return(False)
        for i in range(0, board_len):
            self.resetCount(count)
            for j in range(0, board_len):
                if(board[j][i] != '.'):
                    count[board[j][i]] +=1
                    if(count[board[j][i]]>1):
                        return(False)
        for i in range(0,board_len-2,3):
            for j in range(0, board_len-2,3):
                if(self.judgeSubBox(board,i,j) == False):
                    return(False)
        return(True)
                
    def judgeSubBox(self, board,start_i,start_j):
        count={}
        self.resetCount(count)
        for i in range(start_i, start_i+3):
            for j in range(start_j, start_j+3):
                c = board[i][j]
                if(c != '.'):
                    count[c] +=1
                    if(count[c]>1):
                        return(False)
        return(True)
                
        
    def resetCount(self, count):
        for i in self.number:
            count[i] = 0

ss = Solution()

testData = [['5','3','.','.','7','.','.','.','.'],
            ['6','.','.','1','9','5','.','.','.'],
            ['.','9','8','.','.','.','.','6','.'],
            ['8','.','.','.','6','.','.','.','3'],
            ['4','.','.','8','.','3','.','.','1'],
            ['7','.','.','.','2','.','.','.','6'],
            ['.','6','.','.','.','.','2','8','.'],
            ['.','.','.','4','1','9','.','2','5'],
            ['.','.','.','.','8','.','.','7','9']]
result = ss.isValidSudoku(testData)
print(result)