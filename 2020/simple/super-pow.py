from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result = 1
        mod = a % 1337
        if mod <= 1:
            return mod

        while len(b) > 0:
            mod = a % 1337
            a = mod
            times = 0
            while a < 1337:
                a = a * mod
                times += 1

            a = a / mod
            b, left = self.list_apply(b, times)
            result *= mod * left

        return result % 1337

    @staticmethod
    def list_apply(b: List[int], c) -> (List[int], int):
        result = []

        is_start = False
        t = 0
        for num in b:
            t = t * 10 + num
            apply = int(t / c)
            if is_start is False and apply > 0:
                is_start = True
                result.append(apply)
            elif is_start is True:
                result.append(apply)

            t = t % c

        return result, t

print(Solution().superPow(a = 2, b = [3]))
