class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        count = 0
        i=1
        while(True):
            curr = n//(5**i)
            if curr == 0:
                break
            else:
                count += curr
                i +=1
        return(count)
ss = Solution()
num = 25
result= ss.trailingZeroes(num)
print(result)
count =1
ZeroCount = 0
for i in range(1, num+1):
    count *=i
   
print(count)
print(ZeroCount)