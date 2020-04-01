class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s is None:
            return 0

        statistic = dict()
        for char in s:
            if char in statistic:
                statistic[char] += 1
            else:
                statistic[char] = 1
        count = 0
        for key in statistic:
            if statistic[key] % 2 == 0:
                count += statistic[key]
            else:
                count += statistic[key] - 1

        if count < len(s):
            count += 1
        return count


print(Solution().longestPalindrome('abccccdd'))
