class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        A_len = len(A)
        P_0 =0
        P_2 = A_len -1
        num_1_To_0 =0
        num_1_To_2 =0

        if(A_len <=1):
        	return
        while(True):
        	if(P_0 == P_2):
        		if(num_1_To_0 > 0):
        			if(A[P_0] == 0):
        				for x in range(P_0 + 1- num_1_To_0,P_0 + 1):
        					A[x]=1
        			else:
        				for x in range(P_0 - num_1_To_0,P_0):
        					A[x] =1
        		if(num_1_To_2 >0):
        			if(A[P_2] == 2):
        				for x in range(P_2,P_2 + num_1_To_2):
        					A[x] = 1
        			else:
        				for x in range(P_2+1, P_2 +1 + num_1_To_2):
        					A[x] =1
        		return
        	elif(A[P_0] == 0):
        		P_0 +=1
        	elif(A[P_2] == 2):
        		P_2 -=1
        	elif(A[P_0] == 2 and A[P_2] == 0):
        		A[P_0] =0
        		A[P_2] =2
        	elif(A[P_0] == 1):
        		A[P_0] =0
        		num_1_To_0 +=1
        		P_0 +=1
        	elif(A[P_2] ==1):
        		A[P_2] =2
        		num_1_To_2 +=1
        		P_2 -=1



ss=Solution()
A=[1,0]
ss.sortColors(A)
print(A)