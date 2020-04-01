from typing import List


class Solution:
    def __init__(self):
        self.board = None

    def numRookCaptures(self, board: List[List[str]]) -> int:
        self.board = board
        R_i, R_j = self.findRook()
        if R_i < 0:
            return 0

        return self.checkLeftDirection(R_i, R_j) + \
               self.checkRightDirection(R_i, R_j) + \
               self.checkUpDirection(R_i, R_j) + \
               self.checkDownDirection(R_i, R_j)

    def findRook(self) -> (int, int):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 'R':
                    return i, j
        return -1, -1

    def checkLeftDirection(self, R_i: int, R_j: int) -> int:
        R_j -= 1
        while R_j >= 0:
            if self.board[R_i][R_j] == 'p':
                return 1
            elif self.board[R_i][R_j] == 'B':
                return 0
            R_j -= 1

        return 0

    def checkRightDirection(self, R_i: int, R_j: int) -> int:
        R_j += 1
        while R_j < 8:
            if self.board[R_i][R_j] == 'p':
                return 1
            elif self.board[R_i][R_j] == 'B':
                return 0
            R_j += 1

        return 0

    def checkUpDirection(self, R_i: int, R_j: int) -> int:
        R_i -= 1
        while R_i >= 0:
            if self.board[R_i][R_j] == 'p':
                return 1
            elif self.board[R_i][R_j] == 'B':
                return 0
            R_i -= 1

        return 0

    def checkDownDirection(self, R_i: int, R_j: int) -> int:
        R_i += 1
        while R_i < 8:
            if self.board[R_i][R_j] == 'p':
                return 1
            elif self.board[R_i][R_j] == 'B':
                return 0
            R_i += 1

        return 0
