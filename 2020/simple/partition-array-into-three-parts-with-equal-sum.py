from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False

        one_third = int(total / 3)
        count = 0
        temp = 0
        left = 0
        for num in A:
            if count == 3:
                left += num
            else:
                temp += num
                if temp == one_third:
                    count += 1
                    temp = 0

        return count == 3 and left == 0

print(Solution().canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
