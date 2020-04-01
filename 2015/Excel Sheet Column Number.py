class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        result = 0
        unit = 26
        for char in s:
            result = result*26 + ord(char) - 64
        return(result)

ss = Solution()
result = ss.titleToNumber('BC')
print(result)