class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num_len = len(num)
        if(num_len<=1):
            return([num])
        else:
            result = self.permute(num,0,num_len-1)
            return(result)
    def permute(self,num,k,m):
        if(k==m):
            return([[num[m]]])
        used = []
        result = []
        for i in range(k,m+1):
            if(num[i] in used):
                continue
            else:
                used.append(num[i])
                self.swap(num,k,i)
                subResult = self.permute(num,k+1,m)
                for sub in subResult:
                    result.append([num[k]]+sub)
                self.swap(num,i,k)
        return(result)
    def swap(self,num,i,j):
        temp = num[i]
        num[i]=num[j]
        num[j]=temp
ss = Solution()
test = [1,1,2,2]
result = ss.permuteUnique(test)
print(result)
                