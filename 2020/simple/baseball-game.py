from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        valid_points = []
        count = len(ops)
        for i in range(count):
            op = ops[i]
            if op == '+':
                point = 0
                if len(valid_points) > 1:
                    point = valid_points[-1] + valid_points[-2]
                elif len(valid_points) > 0:
                    point = valid_points[-1]
                valid_points.append(point)
            elif op == 'D':
                valid_points.append(valid_points[-1] * 2 if len(valid_points) > 0 else 0)
            elif op == 'C':
                if len(valid_points) > 0:
                    valid_points.pop()
            else:
                valid_points.append(int(op))

        return sum(valid_points)


print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
