class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if(num == None):
            return([])
        num_len = len(num)
        if(num_len == 1):
            return([num])
        else:
            currVal = num[0]
            num.remove(num[0])
            subPermute = self.permute(num)
            result = []
            for permute in subPermute:
                for i in range(0, num_len):
                    newPermute = list(permute)
                    newPermute.insert(i,currVal)
                    result.append(newPermute)
            return(result)
ss = Solution()
test = [1,2,3,4]
result = ss.permute(test)
print(result)
                
            