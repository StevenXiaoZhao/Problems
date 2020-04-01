class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = self.toAlNum(s)
        count = len(clean)
        for x in range(int(count/2)):
            if clean[x] != clean[count-x-1]:
                return False

        return True

    def toAlNum(self, s: str) -> str:
        ss = ''
        if s is None:
            return ss

        for char in s:
            if str.isalnum(char):
                ss += str.lower(char)
        return ss

test = ""
result = Solution().toAlNum(test)
print(result)

result = Solution().isPalindrome(test)
print(result)