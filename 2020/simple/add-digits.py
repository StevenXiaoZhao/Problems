class Solution:
    def addDigits(self, num: int) -> int:

        if num == 0:
            return 0

        result = num % 9
        return result if result > 0 else 9
