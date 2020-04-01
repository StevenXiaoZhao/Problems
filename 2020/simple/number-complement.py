class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num)
        return int('1'*(len(a)-2), 2)-num

print(Solution().findComplement(190458239457))
