class Solution:
    def reverseVowels(self, s: str) -> str:
        s1 = ''
        s2 = ''
        i = 0
        j = len(s) - 1
        vowels = set(['a', 'e', 'u', 'i', 'o', 'A', 'E', 'U', 'I', 'O'])
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s1 += s[j]
                s2 = s[i] + s2
                i += 1
                j -= 1
            elif s[i] not in vowels and not s[j] in vowels:
                s1 += s[i]
                s2 = s[j] + s2
                i += 1
                j -= 1
            elif s[i] not in vowels:
                s1 += s[i]
                i += 1
            elif s[j] not in vowels:
                s2 = s[j] + s2
                j -= 1

        return s1 + s2 if i>j else s1+s[i]+s2


print(Solution().reverseVowels("aA"))
