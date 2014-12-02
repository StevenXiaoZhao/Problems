class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num_len = len(num)
        
        num.sort()
        
        sum_val = num[0] + num[1] + num[2]
        dist = abs(sum_val - target)
        
        for i in range(0, num_len-1):
            j = i +1
            k = num_len-1
            while(j<k):
                temp_sum = num[i]+num[j] + num[k]
                temp_dist = abs(temp_sum - target)
                if(temp_dist == 0):
                    return(temp_sum)
                elif(temp_dist<dist):
                    sum_val = temp_sum
                    dist = temp_dist   
                if(temp_sum > target):
                    k-=1
                else:
                    j+=1
        return(sum_val)

ss = Solution()
test =  [1,-3,3,5,4,1]
result = ss.threeSumClosest(test,1)
print(result)