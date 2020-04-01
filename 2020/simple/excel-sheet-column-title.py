class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        ord_A = ord('A')
        while n >=1:
            t = n%26
            if t == 0:
                t=26
            s=chr(ord_A + t-1)+s
            n = int((n-t)/26)

        return s

print(Solution().convertToTitle(1))