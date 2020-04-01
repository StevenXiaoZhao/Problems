class Solution:
    def toHex(self, num: int) -> str:
        full =4294967296
        if num <0:
            num = full + num
        elif num == 0:
            return '0'
        result = ''
        mapping = ['a', 'b', 'c', 'd', 'e', 'f']
        while num>0:
            t= num%16
            if t >9:
                t = mapping[t-10]
            result= str(t)+result
            num = int(num/16)
        return result
print(Solution().toHex(889))
