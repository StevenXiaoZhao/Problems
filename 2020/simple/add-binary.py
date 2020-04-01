class Solution:
    def addBinary(self, a: str, b: str) -> str:
        count_a = len(a)
        count_b = len(b)
        count = max(count_a, count_b)
        left = 0
        c = ''
        for i in range(count):
            value_a = int(a[count_a - 1 - i] if count_a - 1 - i >= 0 else 0)
            value_b = int(b[count_b - 1 - i] if count_b - 1 - i >= 0 else 0)

            value = left + value_b + value_a

            left = 1 if value >= 2 else 0
            c = str(0 if value % 2 == 0 else 1) + c

        if left > 0:
            c = '1' + c

        return c
print(Solution().addBinary(a = "11", b = "11"))