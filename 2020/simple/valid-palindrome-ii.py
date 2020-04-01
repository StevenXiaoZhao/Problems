class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s is None or len(s) <= 1:
            return True
        count = len(s)
        i = 0
        j = count - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                result1 = False
                result2 = False
                if s[i] == s[j - 1]:
                    result1 = self.isPalindrome(s, i+1, j-2)
                if s[i + 1] == s[j]:
                    result2 = self.isPalindrome(s, i+2, j-1)

                result = result1 or result2
                return result

        return True

    def isPalindrome(self, s, i, j) -> bool:
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

print(Solution().validPalindrome("eeccccbebaeeabebccceea"))