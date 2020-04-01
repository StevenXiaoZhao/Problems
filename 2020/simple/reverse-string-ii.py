class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        count = len(s)
        i = 0
        need_reverse = True
        while i < count:
            temp = s[i:i + k]
            result += temp[::-1] if need_reverse else temp
            need_reverse = not need_reverse
            i += k
        return result


print(Solution().reverseStr(s="abcdefg", k=12))
