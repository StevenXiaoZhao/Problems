__author__ = 'xiaofez'
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        char_set = set([])
        max_length = 0
        if s == '':
            return 0
        i = 0
        for j in range(len(s)):
            if s[j] in char_set:
                while i <= j:
                    if s[i] == s[j]:
                        i += 1
                        break
                    else:
                        char_set.remove(s[i])
                        i += 1
            else:
                char_set.add(s[j])
                if max_length < len(char_set):
                    max_length = len(char_set)
        return max_length
ss = Solution()
test = 'abcdefghilmnf'
print(ss.lengthOfLongestSubstring(test))


