class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        candidates.reverse()
        result = self.combinationSumProcess(candidates, target)
        if(result == None or result ==[[]]):
            return([])
        else:
            return(result)
    def combinationSumProcess(self, candidates, target):
        can_len = len(candidates)
        if(target == 0):
            return([[]])
        elif(can_len == 0):
            return(None)
        else:
            result = []
            curr = candidates[0]
            left = list(candidates)
            left.remove(left[0])
            if(target<curr):
                return(self.combinationSumProcess(left,target))
            elif(target == curr):
                result.append([curr])
                subResult = self.combinationSumProcess(left,target)
                if(subResult != None and subResult != [[]]):
                    for sub in subResult:
                        result.append(sub)
                return(result)
            else:
                count = target//curr
                if(len(left) == 0):
                    if(count * curr == target):
                        return[[curr]*count]
                    else:
                        return(None)
                for i in range(count+1):
                    num = i*curr
                    newTarget = target - num
                    subResult = self.combinationSumProcess(left,newTarget)
                    if(subResult != None):
                        if(subResult == [[]]):
                            if(num !=0):
                                result.append([curr]*i)
                        else:
                            if(num == 0):
                                for sub in subResult:
                                    result.append(sub)
                            else:
                                for sub in subResult:
                                    sub.extend([curr]*i)
                                    result.append(sub)
                if(result == []):
                    return(None)
                else:
                    return(result)
ss = Solution()
result = ss.combinationSum([2],1)
print(result)
        