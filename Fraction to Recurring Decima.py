class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return('0')
        sign = numerator//abs(numerator) * denominator//abs(denominator)
        denominator = abs(denominator)
        numerator = abs(numerator)
        integerPart = numerator // denominator
        
        numerator = numerator % denominator
        if numerator == 0:
            if sign < 0 and integerPart >0:
                integerPart = - integerPart
            return(str(integerPart))
        factors=[]
        residues = []
        residue = numerator*10
        repeatResidue = -1
        repeatStartNum = -1
        while(True):
            if residue == 0:
                break
            factor = residue // denominator
            residue = residue % denominator
            if (residue in residues):
                for x in range(len(residues)):
                    if residue == residues[x] and factor == factors[x]:
                        repeatResidue = residue
                        repeatStartNum = factor
                        break
            if repeatResidue > -1:
                break
            factors.append(factor)
            residues.append(residue)
            residue = residue *10
        result = ''
        if sign <0:
            result = '-'
        result += str(integerPart) + '.'
        for x in range(len(factors)):
            if residues[x] == repeatResidue and factors[x] == repeatStartNum:
                result += '('
            result += str(factors[x])
        if repeatResidue >= 0:
            result += ')'
        return(result)
ss = Solution()
result = ss.fractionToDecimal(-3, 1)
print(result)
        