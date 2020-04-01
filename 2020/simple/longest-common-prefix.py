from typing import List
import random

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''

        common_prefix = ''
        count = len(strs)
        max_len = len(strs[0])
        for i in range(max_len):
            str1 = strs[random.randint(0, count-1)]
            if i >= len(str1):
                break

            common_char = str1[i]
            if self.isCommonOnSameLocation(strs, i, common_char):
                common_prefix += common_char
            else:
                break

        return common_prefix

    def isCommonOnSameLocation(self, strs: List[str], location: int, common_char: str) -> bool:
        for str1 in strs:
            if location >= len(str1) or str1[location] != common_char:
                return False

        return True

print(Solution().longestCommonPrefix(["aca","cba"]))