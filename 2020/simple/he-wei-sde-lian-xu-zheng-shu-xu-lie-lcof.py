from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        result = []
        count = 2
        while True:
            x = int(target - count*(count+1)/2)
            if x<0:
                break

            if x%count == 0:
                x=int(x/count)
                num = [x+1]*count
                for i in range(1, count):
                    num[i]+=i
                result.insert(0, num)
            count+=1
        return result

print(Solution().findContinuousSequence(15))