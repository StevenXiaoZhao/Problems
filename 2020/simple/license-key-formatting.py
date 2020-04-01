class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        count = len(S)
        p = K
        result = ''
        for j in range(count):
            char = S[count - 1 - j]
            if char != '-':
                if p == 0:
                    p = K
                    result = '-' + result

                p -= 1
                result = char.upper() + result

        return result


print(Solution().licenseKeyFormatting(S="--a-a-a-a--", K=2))
