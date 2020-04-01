from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            data = [[1],[1,1]]
            for i in range(2, numRows):
                source = data[i-1]
                row=[1]
                for j in range(len(source)-1):
                    row.append(source[j]+source[j+1])
                row.append(1)
                data.append(row)

        return data

result =Solution().generate(10)
for data in result:
    print(data)

