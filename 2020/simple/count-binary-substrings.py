class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        j = 0
        count = len(s)
        kinds = 0
        while i < count - 1:
            j = 0
            while i - j >= 0 and i + j + 1 < count and s[i - j] != s[i + j + 1] and s[i - j] == s[i] and s[i + j + 1] == \
                    s[i + 1]:
                kinds += 1
                j+=1

            i = i + 1 if j == 0 else i + j
        return kinds


print(Solution().countBinarySubstrings("10101"))
