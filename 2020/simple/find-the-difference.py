class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = self.list2dict(s)
        for char in t:
            if char not in s_dict or s_dict[char] == 0:
                return char

            s_dict[char]-=1
        return ''


    def list2dict(self, s: str )->dict:
        s_dict = dict()
        for char in s:
            if char not in s_dict:
                s_dict[char] =1
            else:
                s_dict[char] += 1

        return s_dict