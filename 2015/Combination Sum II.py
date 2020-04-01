class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        if(target <=0 or candidates == None):
            return([])
        else:
            candidates.sort()
            result = self.combinationSum(candidates, target)
            return(result)
    def combinationSum(self, candidates, target):
        if(target <=0 or candidates == None):
            return([])
        c_len = len(candidates)
        if(c_len == 1):
            if(candidates[0] == target):
                return([[target]])
            else:
                return([])
        curr = candidates[0]
        if(curr >target):
            return([])
        elif(curr == target):
            return([[curr]])
        result = []
        can_copy1 = list(candidates)
        can_copy1.remove(can_copy1[0])
        can_copy2 = list(can_copy1)

        subResult = self.combinationSum2(can_copy1,target-curr)
        if(subResult != []):
            for sub in subResult:
                result.append([curr]+sub)
        subResult = self.combinationSum2(can_copy2,target)
        if(subResult != []):
            for sub in subResult:
                if(sub in result):
                    continue
                result.append(sub)
        return(result)
ss = Solution()

result = ss.combinationSum2([32,33,5,32,12,7,17,33,29,13,18,16,23,28,26,26,12,6,23,19,22,12,9,6,5,34,22,27,11,33,27,30,24,27,27,31,29,32,21,24,32,5,27,21,20,10,12,28,11,31,12,20,30,17,21,30,8,8], 27)
print(result)
            