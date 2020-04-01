class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        checked = set()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in checked:
                    return False
                checked.add(t[i])
                mapping[s[i]] = t[i]

        return True

print(Solution().isIsomorphic(s = "paper", t = "title"))
