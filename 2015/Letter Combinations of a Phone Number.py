class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        dict = {'2':'abc',
               '3':'def',
               '4':'ghi',
               '5':'jkl',
               '6':'mno',
               '7':'pqrs',
               '8':'tuv',
               '9':'wxyz'}
        if(digits == None):
            return([])
        num = len(digits)
        if(num == 0):
            return([])
        orginal = [0]*num
        iterative_times = 1
        for i in range(num):
            orginal[i] = len(dict[digits[i]])
            iterative_times *= orginal[i]
        changeCircle = [0]*num
        changeCircle[num-1] = 1
        for i in range(num-2,-1,-1):
            changeCircle[i] = orginal[i+1]*changeCircle[i+1]
        result = []
        history = list(orginal)
        for i in range(1, iterative_times+1):
            curr = ''
            for j in range(num):
                curr += dict[digits[j]][history[j] -1]
                if(i%changeCircle[j] == 0):
                    history[j] -=1
                if(history[j] <=0):
                    history[j] = orginal[j]
            result.append(curr)
        return(result)
ss = Solution()
test = '2'
result = ss.letterCombinations(test)
print(result)
        