from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return []
        elif rowIndex == 1:
            return [1]
        elif rowIndex == 2:
            return [1, 1]
        else:
            data = [1]*rowIndex
            for i in range(2, rowIndex):
                temp = data[0]
                for j in range(1, i):
                    temp2=data[j]
                    data[j] = data[j]+temp
                    temp = temp2
        return data

result = Solution().getRow(3)
for data in result:
    print(data)
