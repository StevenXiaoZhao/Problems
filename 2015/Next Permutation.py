class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        num_len = len(num)
        for i in range(num_len -1, 0, -1):
            if(num[i] > num[i-1]):
                num[i-1] = self.findMini(num[i-1], num, i)
                return(num)
        num.reverse()
        return(num)
    def findMini(self, curr, num, index):
        num_len = len(num)
        i = index
        j = num_len -1
        result = num[index]
        while(i<j):
            temp = num[i]
            num[i]= num[j]
            num[j]=temp
            i +=1
            j -=1
        for i in range(index, num_len):
            if(curr<num[i]):
                result = num[i]
                num[i] = curr
                break
        return(result)
        
ss = Solution()
result = ss.nextPermutation([1,2,7,6,5])
print(result)