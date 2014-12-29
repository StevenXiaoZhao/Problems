class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x <=0:
            return(0)
        else:
            x = x*1.0
            val = x/2
            criti = 0.001
            while(abs(val*val-x)>criti):
                val = (val + x/val)/2
            intVal = int(val)
            return(intVal)
ss = Solution()
result = ss.sqrt(1)
print(result)