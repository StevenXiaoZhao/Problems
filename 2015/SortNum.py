class Solution:
	# @param num, a list of integer
	# @return a list of integer
	def nextPermutation(self, num):
		num_len = len(num)
		if num_len <=1:
			return(num)
		is_sorted = 'true'
		for x in range(0, num_len-1):
			if num[x] > num[x+1]:
				is_sorted = 'false'
				break
		if is_sorted == 'true':
			for x in range(num_len-2, -1, -1):
				if num[x] < num[x+1]:
					temp = num[x]
					num[x] = num[x+1]
					num[x+1] = temp
					return(num)
		num.sort()
		return(num)

test = Solution()
result = test.nextPermutation([1,1,2,3,4,4,4,4])

print(result)