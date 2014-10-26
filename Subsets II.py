class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        s_len = len(S)
        if(s_len == 0):
            return([[]])
        else:
            max_s = max(S)
            S.remove(max_s)
            dupCount = 1
            while(len(S)>0 and max_s == max(S)):
                dupCount +=1
                S.remove(max_s)
            s_subsets = self.subsetsWithDup(S)
            dupResult = []
            if(dupCount >1):
                for i in range(0, dupCount):
                    elements = [max_s]
                    for j in range(0,i):
                        elements.append(max_s)
                    dupResult.append(elements)
            result = []
            for subset in s_subsets:
                result.append(subset)
                if(dupCount > 1):
                    for dup in dupResult:
                        newSet = list(subset)
                        newSet.extend(dup)
                        result.append(newSet)
                else:
                    newSet = list(subset)
                    newSet.append(max_s)
                    result.append(newSet)

            return(result)
ss = Solution()
s = [5,5,5,5,5,5]
result = ss.subsetsWithDup(s)
print(result)        
        