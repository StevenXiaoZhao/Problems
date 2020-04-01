class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        x=1
        y=1
        for i in range(2, N):
            x, y = y, x
            x=y+x

        return x

print(Solution().fib(4))