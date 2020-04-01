class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None and t is None:
            return True

        if s is None or t is None:
            return False

        if len(s) != len(t):
            return False

        s_chars = self.getCharCountDict(s)
        t_chars = self.getCharCountDict(t)

        if len(s_chars.keys()) != len(t_chars.keys()):
            return False
        for k in s_chars:
            if k not in t_chars or t_chars[k] != s_chars[k]:
                return False

        return True

    @staticmethod
    def getCharCountDict(s: str) -> dict:
        result = dict()
        for char in s:
            if char in result:
                result[char] += 1
            else:
                result[char] = 1

        return result