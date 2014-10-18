class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if(num == None):
            return(0)
        mirror = {}
        num_len = len(num)
        for i in num:
            if( (i in mirror) == False):
                mirror[i] = 1
        max_len = 1
        part_len = 1
        first = True
        prev = 0
        for x in mirror:
            if(first):
                prev = x
                first = False
            else:
                if(x >=0 and x == prev + 1):
                    part_len+=1
                elif( x <0 and x == prev -1):
                    part_len+=1
                else:
                    part_len = 1
                if(part_len > max_len):
                    max_len = part_len
                prev = x
        result = 0
        if 0 in mirror:
            i =1
            while(i in mirror):
                i +=1
            j =-1
            while(j in mirror):
                j -=1                
            result = i - j -1
        if(result> max_len):
            max_len = result
        return(max_len)
a =  [-1,-9,-5,-2,-9,8,-8,1,-9,-3,-3] 
ss= Solution()

result = ss.longestConsecutive(a)
print(result)
        