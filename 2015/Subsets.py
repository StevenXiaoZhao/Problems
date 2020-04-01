class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        s_len = len(S)
        if(s_len == 0):
            return([[]])
        else:
            max_s = max(S)
            S.remove(max_s)
            s_subsets = self.subsets(S)
            result = []
            for subset in s_subsets:
                newSet = list(subset)
                newSet.append(max_s)
                result.append(subset)
                result.append(newSet)
            return(result)
ss = Solution()
s = [1,2,3]
result = ss.subsets(s)
print(result)
        