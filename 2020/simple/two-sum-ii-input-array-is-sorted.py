from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        i = 0
        while i<j:
            sum_num = numbers[i] + numbers[j]
            if sum_num == target:
                return [i+1, j+1]
            elif sum_num < target:
                i += 1
            else:
                j -= 1

        return None


testData = [1, 4, 4, 7, 11, 15]
target = 8
print(Solution().twoSum(testData, target))