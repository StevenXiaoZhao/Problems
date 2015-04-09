__author__ = 'xiaofez'
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if num == []:
            return []
        num.sort()
        result = []
        for i in range(0, len(num)-2):
            if num[i] == 0:
                if num[i+1] == 0 and num[i+2] == 0:
                    result.append([0,0,0])
                break
        j = 2
        i = 2
        while i < len(num):
            while j < len(num) and num[j] == num[j-2]:
                j += 1
            if j >= len(num):
                num = num[0:i]
                break
            elif i != j:
                num[i] = num[j]

                if j + 1 < len(num) and num[j] == num[j+1]:
                    num[i+1] = num[j+1]
                    i += 1
                    j += 1
            j += 1
            i += 1
        num_len = len(num)
        prev = num[0]
        for i in range(1, num_len):
            curr = num[i]
            j = 0
            if prev == curr:
                j = i-1
            else:
                prev = curr
            k = num_len - 1
            while j < i and k > i :
                if num[j] + num[k] == -curr:
                    find = [num[j], curr, num[k]]
                    result.append(find)
                    j += 1
                    k -= 1
                    if j < i and j >0 and num[j] == num[j-1]:
                        j += 1
                    if k > i and k < num_len -1 and num[k] == num[k+1]:
                        k -= 1
                elif num[j] + num[k] > -curr:
                        k -= 1
                else:
                        j += 1
        return result
ss = Solution()
test = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
result = ss.threeSum(test)
print(result)
