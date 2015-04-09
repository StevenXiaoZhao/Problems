__author__ = 'xiaofez'
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        numbers1 = [0]*len(num1)
        numbers2 = [0]*len(num2)
        result = [0]*(len(num1) + len(num2))
        for i in range(len(num1)):
            numbers1[i] = int(num1[i])
        for i in range(len(num2)):
            numbers2[i] = int(num2[i])
        dict = self.computeBase(numbers1)
        startIndex = len(result) - 1

        for i in range(len(numbers2)-1, -1, -1):
            curr = dict[numbers2[i]]
            add = 0
            j = startIndex
            k = len(curr) - 1
            while j >= 0 and k >= 0:
                val = result[j] + curr[k] + add
                add = val//10
                result[j] = val%10
                j -= 1
                k -= 1
            if add != 0 and j >= 0:
                result[j] = add
            startIndex -= 1
        #generate string
        string = ''
        isStartZero = True
        for x in result:
            if x != 0 and isStartZero:
                isStartZero = False
            if isStartZero == False:
                string += str(x)
        if string == '':
            string = '0'
        return(string)

    def computeBase(self, num):
        dict={}
        dict[0] = [0] * (len(num) + 1)
        dict[1] = [0] + list(num)

        for i in range(2, 10):
            add = 0
            curr = [0]*(len(num) + 1)
            for j in range(len(num), 0, -1):
                result = dict[i-1][j] + num[j-1] + add
                add = result//10
                curr[j] = result % 10
            curr[0] = add + dict[i-1][0]
            dict[i] = curr
        return dict

ss = Solution()
result = ss.computeBase([9,9,9,9,9,9,9,9])
print(result)
result = ss.multiply("1","9999999999999999999999999999999999999999999999999999999")
print(result)