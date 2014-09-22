class Solution:
    # @return a string
    def intToRoman(self, num):
    	roman = ''
    	i=0
    	while(True):
        	left = num % 10
        	if(num ==0 and left ==0):
        		return roman
        	else:
        		roman = self.GetRomanByBit(left,i) + roman
        	num = num //10
        	i +=1
        		


    transfer = ['I','V','X','L','C','D','M']
    def GetRomanByBit(self,num, bit):
    	transfer_len = len(self.transfer)
    	num_1 = self.transfer[bit*2]
    	if(num<4):
    		return num*num_1
    	elif(num == 4):
    		num_5 = self.transfer[bit*2+1]
    		return num_1 + num_5
    	elif(num <9):
    		num_5 = self.transfer[bit*2+1]
    		return num_5 + (num-5)*num_1
    	else:
    		num_big = self.transfer[bit*2+2]
    		return num_1 + num_big

ss= Solution()

print(ss.intToRoman(3999))