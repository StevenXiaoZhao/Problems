class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        numSet = set(num)
        for x in numSet:
            t = target - x
            if t in numSet:
                index1 = -1
                index2 = -1
                for i in range(len(num)):
                    if num[i] == x or num[i] == t:
                        if index1 == -1:
                            index1 = i + 1
                        elif index2 == -1:
                            index2 = i + 1
                            break
                return([index1,index2])
ss = Solution()
result = ss.twoSum([2,7,11,15], 9)
print(result)
              
                            
        