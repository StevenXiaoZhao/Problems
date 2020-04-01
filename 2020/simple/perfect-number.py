class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 != 0:
            return False

        num_sum = 1
        factor = 2
        while factor * factor < num:
            if num % factor == 0:
                num_sum += factor
                num_sum += int(num / factor)

            factor += 1
        return num_sum == num

print(Solution().checkPerfectNumber(6))
