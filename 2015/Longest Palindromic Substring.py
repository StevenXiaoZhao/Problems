__author__ = 'xiaofez'
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if s == '':
            return s
        s_len = len(s)
        max_sub = s[0]
        max_len = 1

        for i in range(s_len-1):
            if s[i] == s[i+1]:
                left_index = i
                right_index = i+1
                [sub_len, sub_str] = self.findPalindome(left_index, right_index, s)
                if sub_len > max_len:
                    max_len = sub_len
                    max_sub = sub_str
            if i > 0 and s[i-1] == s[i+1]:
                left_index = i-1
                right_index = i+1
                [sub_len, sub_str] = self.findPalindome(left_index, right_index, s)
                if sub_len > max_len:
                    max_len = sub_len
                    max_sub = sub_str
        return max_sub
    def findPalindome(self, left_index, right_index, s):
        s_len = len(s)
        while left_index >= 0 and right_index < s_len:
            if s[left_index] != s[right_index]:
                break
            else:
                left_index -= 1
                right_index += 1

        sub_len = right_index - left_index - 1
        sub_paralindome = s[left_index+1:right_index]
        return [sub_len, sub_paralindome]
ss = Solution()
result = ss.longestPalindrome('ccc')
print(result)