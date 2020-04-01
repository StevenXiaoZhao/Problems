class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        return ' '.join(map(lambda word: word[::-1], words))

print(Solution().reverseWords("jad"))