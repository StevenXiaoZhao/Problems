class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        else:
            if len(needle) == 0:
                return 0
            else:
                if len(needle) == len(haystack):
                    if needle == haystack:
                        return 0
                    else:
                        return -1
                else:
                    return haystack.find(needle)

print(Solution().strStr("a","a"))

