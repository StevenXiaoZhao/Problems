class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a >= 0 and b >= 0:
            result = self.plus(bin(a), bin(b))
        elif a < 0 and b < 0:
            result = -self.plus(bin(-a), bin(-b))
        else:
            is_below_zero = (a < 0 and abs(a) > abs(b)) or (b < 0 and abs(b) > abs(a))
            a = int(abs(a))
            b = int(abs(b))
            result = self.minus(a, b) if a > b else self.minus(b, a)
            result = -result if is_below_zero else result
        return result

    def plus(self, s_a, s_b) -> int:
        count_a = len(s_a)
        count_b = len(s_b)
        count = max(count_a, count_b)
        s = ''
        left = 0

        for i in range(count):
            v_a = int(s_a[count_a - 1 - i] if count_a - 1 - i > 1 else 0)
            v_b = int(s_b[count_b - 1 - i] if count_b - 1 - i > 1 else 0)
            if v_a & v_b & left == 1:  # 3
                left = 1
                s = '1' + s
            elif v_a | v_b | left == 0:  # 0
                left = 0
                s = '0' + s
            elif v_a | v_b == 0 or v_a | left == 0 or left | v_b == 0:  # 1
                left = 0
                s = '1' + s
            else:
                left = 1
                s = '0' + s

        return int('0b' + str(left) + s, 2)

    # s_a-s_b
    def minus(self, a: int, b: int) -> int:
        s_a = bin(a)
        s_b = bin(b)

        count_a = len(s_a)
        count_b = len(s_b)
        count = max(count_a, count_b)
        s = ''
        left = 0

        for i in range(count):
            v_a = int(s_a[count_a - 1 - i] if count_a - 1 - i > 1 else 0)
            v_b = int(s_b[count_b - 1 - i] if count_b - 1 - i > 1 else 0)
            if v_a == 0:
                if v_b == 1 and left == 1:
                    left = 1
                    t = '0'
                elif v_b == 1 or left == 1:
                    left = 1
                    t = '1'
                else:
                    left = 0
                    t = '0'
            else:
                if v_b == 1 and left == 1:
                    left = 1
                    t = '1'
                elif v_b == 1 or left == 1:
                    left = 0
                    t = '0'
                else:
                    left = 0
                    t = '1'
            s = t + s

        return int('0b' + str(left) + s, 2)

print(Solution().getSum(20, 30))