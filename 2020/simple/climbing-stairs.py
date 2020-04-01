class Solution:
    def climbStairs(self, n: int) -> int:
        temp = 1
        t = 2
        num = 0

        if n <=2:
            return n
        else:
            for i in range(2, n):
                num = temp + t
                temp = t
                t = num

        return num

print(Solution().climbStairs(4))