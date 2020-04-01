class Solution:
    # @param s, a string
    # @return an integer
    # 0 is the most important issue, just 10 and 20 is valid
    def numDecodings(self, s):
        if s == "":
            return(0)
        if s[0] =='0':
            return(0)
        s_len = len(s)
        nums = [0]*s_len
        nums[0] = 1
        for i in range(1, s_len):
            if s[i] != '0':
                nums[i] = nums[i-1]
            if s[i-1:i+1] == '00':
                return(0)
            elif s[i-1] == '0':
                continue
            big = int(s[i-1:i+1])
            if big <=26:
                if i <=1:
                    nums[i] += 1
                else:
                    nums[i] += nums[i-2]
        return(nums[s_len-1])
ss = Solution()
result = ss.numDecodings("10011")
print(result)