__author__ = 'xiaofez'
class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        if dungeon is None:
            return 0
        row_count = len(dungeon)
        col_count = len(dungeon[0])
        cost = []
        for i in range(row_count):
            cost.append([0]*col_count)
        for i in range(row_count-1, -1, -1):
            for j in range(col_count-1, -1, -1):
                choose = 0
                if j == col_count-1 and i == row_count-1:
                    choose = 0
                elif j == col_count-1:
                    choose = cost[i+1][j]
                elif i == row_count-1:
                    choose = cost[i][j+1]
                else:
                    if cost[i+1][j] > cost[i][j+1]:
                        choose = cost[i+1][j]
                    else:
                        choose = cost[i][j+1]
                #we need to know if current is negitive and following need is positive
                #the positive is not useful for we can't pass this room to get that power
                if dungeon[i][j] >= 0 or choose < 0:
                    cost[i][j] = choose + dungeon[i][j]
                else:
                    cost[i][j] = dungeon[i][j]
        health = 1 if cost[0][0] > 0 else -cost[0][0] + 1
        return health

ss = Solution()
test =[[2],[1]]
print(ss.calculateMinimumHP(test))

