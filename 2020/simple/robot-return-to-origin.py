class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves is None or moves == '':
            return True

        if len(moves)%2 !=0:
            return False

        move_direct = dict()
        move_direct['R'] = 0
        move_direct['L'] = 0
        move_direct['U'] = 0
        move_direct['D'] = 0
        for move in moves:
            move_direct[move] +=1

        return move_direct['R'] == move_direct['L'] and move_direct['U'] == move_direct['D']

print(Solution().judgeCircle("DD"))