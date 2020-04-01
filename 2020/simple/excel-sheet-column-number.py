class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for char in s:
            result = result*26+ord(char)-64

        return result

print(Solution().titleToNumber("A"))