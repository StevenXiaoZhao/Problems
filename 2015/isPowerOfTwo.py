class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        two_power_ten = 1024
        two_power_five = 32
        while n > 1:
            if n >= two_power_ten:
                if n % two_power_ten != 0:
                    return False
                else:
                    n = n >> 10
            elif n >= two_power_five:
                if n % two_power_five != 0:
                    return False
                else:
                    n = n >> 5

            elif n >= 2:
                if n % 2 != 0:
                    return False
                else:
                    n = n >> 1
        return n == 1


print(Solution().isPowerOfTwo(1024))
