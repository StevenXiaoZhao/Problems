class Solution:
    def convertToBase7(self, num: int) -> str:
        is_below_zero = num < 0
        num = abs(num)
        if num == 0:
            return '0'
        result = ''
        while num > 0:
            result = str(num % 7) + result
            num = int(num / 7)
        if is_below_zero:
            result = '-' + result

        return result

print(Solution().convertToBase7(-7))