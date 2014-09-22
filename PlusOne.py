class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
    	digits_len = len(digits)
    	is_plus = False
    	for x in range(digits_len-1, -1,-1):
        	if(digits[x]==0):
        		digits[x] = 1
        		is_plus = True
        		break
        	else:
        		digits[x] = 0
    	if(is_plus == False):
        	result = [1]
        	result.extend(digits)
    	else:
        	result = digits
    	return result

ss= Solution()
result = ss.plusOne([1,0,1,1,1,1])
print(result)
        	