class Solution:
    def mySqrt(self, x: int) -> int:
        start=0
        end=x

        while start <= end:
            test =int( (start+end)/2)
            value = test*test
            if x == value:
                return test
            elif x > value:
                value1 = (test+1)*(test+1)
                if value1 > x:
                    return test
                start = test
            else:
                end = test


