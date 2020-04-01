class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        x = int(num / 2)
        y = x * x
        while True:
            if y == num:
                return True
            elif y < num < (x + 1) * (x + 1):
                return False
            x = int((x + num / x) / 2)
            y = int(x * x)

print(Solution().isPerfectSquare(626))