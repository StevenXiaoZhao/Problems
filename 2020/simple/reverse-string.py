from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        if s is None or len(s) == 0:
            return
        i = 0
        j = len(s)-1
        while i<j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1

t=["H","a","n","b","a","h"]
Solution().reverseString(t)
print(t)