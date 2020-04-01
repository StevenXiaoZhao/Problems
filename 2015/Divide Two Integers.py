class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return(2147483647)
        sign =1
        if dividend <0 or divisor <0:
            if dividend >0 or divisor >0:
                sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        factor = 0
        residue = dividend
        q = 0
        while((divisor << q) < dividend):
            q +=1
        while(residue > 0 and q >=0):
            currDivisor = (divisor << q)
            if residue - currDivisor >= 0:
                factor += (1 << q)
                residue = residue - currDivisor
            q -= 1
            
        if sign <0:
            factor = - factor
        if factor > 2147483647:
            factor = 2147483647
        return(factor)
ss = Solution()
result = ss.divide(1004958205, -2137325331)
print(result)
        