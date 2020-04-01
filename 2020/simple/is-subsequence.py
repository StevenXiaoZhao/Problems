class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return False

        t_dict = self.str2dict(t)
        for char in s:
            if char not in t_dict:
                return False

        count_s = len(s)
        count_t = len(t)
        i_t = 0
        i_s = 0
        while i_s < count_s and i_t < count_t:
            if count_s - i_s > count_t - i_t:
                return False

            index = t_dict[s[i_s]]
            if index >= i_t:
                i_t = index + 1
                i_s += 1
            elif t[i_t] == s[i_s]:
                i_t += 1
                i_s += 1
            else:
                i_t += 1

        return i_s == count_s

    def str2dict(self, s: str) -> dict:
        s_dict = dict()
        count = len(s)
        for i in range(count):
            if s[i] not in s_dict:
                s_dict[s[i]] = i

        return s_dict

print(Solution().isSubsequence(s = "abc", t = "ahbgdc"))
