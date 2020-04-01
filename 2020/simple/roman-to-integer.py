class Solution:
    def romanToInt(self, s: str) -> int:
        data = 0
        if s is None or len(s) == 0:
            return 0
        count = len(s)
        i = 0
        while i < count:
            if s[i] == 'I':
                if i + 1 < count and s[i + 1] == 'V':
                    data += 4
                    i += 1
                elif i + 1 < count and s[i + 1] == 'X':
                    data += 9
                    i += 1
                else:
                    data += 1
            elif s[i] == 'V':
                data += 5
            elif s[i] == 'X':
                if i + 1 < count and s[i + 1] == 'L':
                    data += 40
                    i += 1
                elif i + 1 < count and s[i + 1] == 'C':
                    data += 90
                    i += 1
                else:
                    data += 10
            elif s[i] == 'L':
                data += 50
            elif s[i] == 'C':
                if i + 1 < count and s[i + 1] == 'D':
                    data += 400
                    i += 1
                elif i + 1 < count and s[i + 1] == 'M':
                    data += 900
                    i += 1
                else:
                    data += 100
            elif s[i] == 'D':
                data += 500
            elif s[i] == 'M':
                data += 1000

            i += 1
        return data


print(Solution().romanToInt("MCMXCIV"))
