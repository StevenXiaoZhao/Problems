class Solution:
    def toLowerCase(self, s: str) -> str:
        ss = ''
        for s1 in s:
            if s1.islower():
                ss+=s1
            else:
                ss+=s1.lower()
        return ss
print(Solution().toLowerCase(s = "LOVELY"))