class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if(S == None or T == None):
            return(0)
        S_len = len(S)
        T_len = len(T)
        if(S_len < T_len):
            return(0)
        else:
            result = [1]+[0]*T_len
            for i in range(1, S_len + 1):
                for j in range(T_len, 0, -1):
                    if(S[i-1] == T[j-1]):
                        result[j] += result[j-1]
            return(result[T_len])
        

ss = Solution()
result = ss.numDistinct('b','b')
print(result)
                    