__author__ = 'xiaofez'
import collections
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        dict = self.getDictFromNums(num)
        sorted_dict = collections.OrderedDict(sorted(dict.items()))
        string = ''
        for key in sorted_dict:
            for val in sorted_dict[key]:
                string = str(val) + string
        return string

    def getDictFromNums(self, num):
        max_num = max(num)
        max_digit = 1
        while max_num//10 > 0:
            max_digit += 1
            max_num //= 10
        dict = {}
        max_num = max(num)
        for val in num:
            if val == max_num:
                dict[val] = [val]
            else:
                digit = 1
                last_digit = val
                while last_digit//10 > 0:
                    digit += 1
                    last_digit //= 10
                    last_digit = last_digit
                key = -1
                if digit == max_digit:
                    key = val
                else:
                    key = val * 10 * (max_digit - digit)
                    left = last_digit
                    for x in range(max_digit - digit - 1):
                        left = left * 10 + last_digit
                    key += left
                if key in dict:
                    dict[key].append(val)
                else:
                    dict[key] = [val]
        return dict

ss = Solution()
test = [3, 33, 34, 5, 9]
result = ss.largestNumber(test)
print(result)