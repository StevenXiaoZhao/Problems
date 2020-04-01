class Solution:
    def trailingZeroes(self, n: int) -> int:
        ele = 5
        result = 0
        while n>=5:
            n= int(n/ele)
            result += n

        return result

print(Solution().trailingZeroes(3))