class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power_ten = 59049
        power_five = 243
        power_one = 3
        while n > power_one-1:
            if n >= power_ten:
                if n % power_ten != 0:
                    return False
                else:
                    n = n/power_ten
            elif n >= power_five:
                if n % power_five != 0:
                    return False
                else:
                    n = n/power_five

            elif n >= power_one:
                if n % power_one != 0:
                    return False
                else:
                    n = n/power_one
        return n == 1


print(Solution().isPowerOfThree(2))
