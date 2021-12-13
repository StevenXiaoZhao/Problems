from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            if num < 10:
                result.append(num)
            else:
                curr = num
                good_num = True
                while curr > 0:
                    x = curr % 10
                    if x == 0 or num % x != 0:
                        good_num = False
                        break
                    else:
                        curr = int(curr / 10)

                if good_num:
                    result.append(num)
        return result


print(Solution().selfDividingNumbers(1,22))