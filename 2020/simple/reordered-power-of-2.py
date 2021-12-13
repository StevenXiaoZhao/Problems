from typing import List


class Solution:
    def __init__(self):
        self.pow_2 = [32, 16, 8, 4, 2]

    def reorderedPowerOf2(self, n: int) -> bool:
        digits = []
        if n == 1:
            return True

        while n > 0:
            digits.append(n % 10)
            n = int(n / 10)
        result = []
        for digit in digits:  # 对于每一个末位的考虑
            if digit % 2 != 0:
                continue

            digit_sub = digits.copy()
            digit_sub.remove(digit)
            candidates = self.construct_num(digit_sub)
            for candidate in candidates:
                if candidate != 0:
                    result.append(candidate * 10 + digit)

        for num in result:
            if self.is_2_pow(num):
                print(num)
                return True

        return False

    def is_2_pow(self, num):
        for pow_2_elem in self.pow_2:
            while num >= pow_2_elem:
                if num % pow_2_elem != 0:
                    return False
                num /= pow_2_elem

        return num == 1

    def construct_num(self, digits: List) -> List:
        if len(digits) == 1:
            return [digits.pop()]

        result = []
        for val in digits:
            new_digits = digits.copy()
            new_digits.remove(val)
            sub_nums = self.construct_num(new_digits)
            for sub_num in sub_nums:
                if sub_num != 0:
                    result.append(sub_num * 10 + val)

        return result


print(Solution().reorderedPowerOf2(1521))
