class Solution:
    def isHappy(self, n: int) -> bool:
        checked = set()
        checked.add(n)
        while n !=1:
            n = self.divide(n)
            if n in checked:
                return False

            checked.add(n)
        return True

    def divide(self, n) -> int:
        result = 0
        while n > 0:
            t = n % 10
            result += t * t
            n = int(n / 10)
        return result

print(Solution().isHappy(9999))