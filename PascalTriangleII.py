class Solution:
	# @return a list of lists of integers
	def getRow(self, rowIndex):
		if(rowIndex ==0):
			return([1])
		length = rowIndex +1
		row =[0]*length
		row[length-1]=1
		row[length-2]=1
		
		for x in range(length-3,-1,-1):
			row[x]=1
			for i in range(x+1,length-1):
				row[i]=row[i]+row[i+1]
		return(row)
ss= Solution()
result = ss.getRow(0)
print(result)