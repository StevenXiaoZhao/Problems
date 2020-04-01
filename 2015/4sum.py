__author__ = 'xiaofez'
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num_len = len(num)
        num.sort()
        result = []
        for i in range(num_len - 3):
            if i > 0 and num[i] == num[i-1]:
                continue
            for j in range(i+1, num_len - 2):
                if j > i+1 and num[j] == num[j-1]:
                    continue
                k = j + 1
                z = num_len - 1

                search_val = target - num[i] - num[j]
                while k < z:
                    if num[k] + num[z] == search_val:
                        if k > j+1 and num[k] == num[k-1]:
                            k += 1
                        else:
                            result.append([num[i], num[j], num[k], num[z]])
                            k += 1
                            z -= 1
                    elif num[k] + num[z] > search_val:
                        z -= 1
                    else:
                        k += 1
        return result
ss = Solution()

result = ss.fourSum([1, 0, -1, 0, -2, 2], 0)
print(result)