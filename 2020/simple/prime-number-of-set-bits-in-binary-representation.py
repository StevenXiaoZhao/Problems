class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for num in range(left, right + 1):
            if Solution.is_prime(num) is True:
                count += 1

        return count

    @staticmethod
    def is_prime(num: int) -> bool:
        if num == 2 or num == 3:
            return True

        if num % 2 == 0 or num % 3 == 0:
            return False

        t = int(num / 2)
        if t % 2 == 0:
            t -= 1
        while t > 3:
            if num % t == 0:
                return False
            t -= 2

        return True

print(Solution().countPrimeSetBits(left = 6, right = 10))
