class Solution:
    # @return a string
    def getPermutation(self, n, k):
        nums = [0]*n
        for i in range(n):
            nums[i] = i +1
        return(self.getPermutationFromRange(nums,k-1))
    
    def getPermutationFromRange(self, nums, k):
        n = len(nums)
        if n == 1:
            return(str(nums[0]))
        elif k == 0:
            result = ""
            for num in nums:
                result += str(num)
            return(result)
        count_n = 1
        for i in range(2, n):
            count_n = count_n*i
        index = k //count_n
        num = nums[index]
        nums.remove(num)
        k = k - index*count_n
        follows = self.getPermutationFromRange(nums, k)
        return(str(num)+follows)
ss = Solution()
result = ss.getPermutation(9,100)
print(result)