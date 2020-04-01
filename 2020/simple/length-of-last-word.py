class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        num = 0
        count = len(s)
        for i in range(count):
            if s[count-1-i] == ' ':
                if num == 0:
                    continue
                else:
                    return num
            else:
                num += 1

        return num

print(Solution().lengthOfLastWord('hello'))
