__author__ = 'xiaofez'
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) <= 1:
            return 0
        max_val = max(num)
        min_val = min(num)
        b = min_val
        a = (max_val - b)
        sorted_num = [-1]*len(num)
        sorted_num[0] = min_val
        sorted_num[-1] = max_val
        for i in range(1, len(num)-1):
            number = num[i]
            if number == min_val or number == max_val:
                sorted_num.remove(-1)
                continue
            index = (number-b)*(len(sorted_num)-1)//a
            if sorted_num[index] == -1:
                sorted_num[index] = number
            else:
                curr = number
                while sorted_num[index] != -1:
                    if curr >= sorted_num[index]:
                        index += 1
                    else:
                        temp = sorted_num[index]
                        sorted_num[index] = curr
                        curr = temp
                        index += 1
                    if index > len(sorted_num)-1:
                        break
                if index < len(sorted_num)-1:
                    sorted_num[index] = curr
        #find the largest distant
        print(sorted_num)
        max_len = 0
        pre = sorted_num[0]
        for number in sorted_num:
            curr_len = number - pre
            pre = number
            if curr_len > max_len:
                max_len = curr_len
        return max_len
ss = Solution()
test = [15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]
print(ss.maximumGap(test))
