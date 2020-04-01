import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        if n == 3:
            return 1

        count = 1
        for i in range(3, n, 2):
            if self.isPrimes(i):
                print(i)
                count += 1

        return count

    def isPrimes(self, n: int) -> bool:
        if n % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False

        return True


print(Solution().countPrimes(499979))
