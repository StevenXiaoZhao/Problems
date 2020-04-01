class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s is None or s =='':
            return -1
        s_dict = dict()
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        count = len(s)
        for i in range(count):
            if s_dict[s[i]] ==1:
                return i
        return -1

print(Solution().firstUniqChar('leetcode'))
