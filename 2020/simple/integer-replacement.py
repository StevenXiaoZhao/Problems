class Solution:
    def integerReplacement(self, n: int) -> int:
        if n <= 1:
            return 0

        times = 0
        while n > 1:
            times += 1
            if n % 2 == 0:
                n = n >> 1
            elif n == 3:
                n = 2
            elif n & 3 == 1:
                n -= 1
            else:
                n += 1
        return times


print(Solution().integerReplacement(65535))
