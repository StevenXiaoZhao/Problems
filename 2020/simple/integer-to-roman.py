class Solution:
    def intToRoman(self, num: int) -> str:
        t = int(num/1000)
        roman = t*'M'

        num = num - t*1000
        t = int(num/100)
        roman += self.compute(t, 'C', 'D', 'M')

        num = num - t * 100
        t = int(num / 10)
        roman += self.compute(t, 'X', 'L', 'C')

        num = num - t * 10
        roman += self.compute(num, 'I', 'V', 'X')
        return roman

    @staticmethod
    def compute(t, one, five, ten) -> str:
        roman = ''
        if t == 9:
            roman += one + ten
        elif t == 4:
            roman += one + five
        else:
            if t >= 5:
                roman += five
                roman += one * (t - 5)
            else:
                roman += one * t
        return roman

print(Solution().intToRoman(1994))