class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        s_len = len(s)
        pair = []
        for i in range(s_len):
            pair.append([False]*s_len)
            pair[i][i] = True
        for i in range(s_len - 1, -1, -1):
            for j in range(i+1, s_len):
                if(j-i == 1):
                    if(s[i] == s[j]):
                        pair[i][j] = True
                else:
                    if(s[i] == s[j] and pair[i+1][j-1] == True):
                        pair[i][j] = True
        subStrs = {}
        for i in range(s_len):
            