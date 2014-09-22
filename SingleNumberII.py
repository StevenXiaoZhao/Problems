class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dic = {}
        A_len = len(A)
        for x in range(0,A_len):
        	if(A[x] in dic):
        		dic[A[x]]+=1
        	else:
        		dic[A[x]]=1
        dic_len = len(dic)
        for key in dic:
        	if(dic[key]!=3):
        		return (key)
        return(-1)

ss =Solution()

result = ss.singleNumber([1,2,1,3,2,1,2,3,5,3])
print(result)