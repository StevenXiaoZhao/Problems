class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if(num == None):
            return(None)
        else:
            return(self.findMinInRange(num,0, len(num)-1))
    def findMinInRange(self, num, startIndex, endIndex):
        if(startIndex == endIndex):
            return(num[startIndex])
        elif(num[startIndex] < num[endIndex]):
            return(num[startIndex])
        else:                
            midIndex = (startIndex + endIndex)//2
            if(midIndex == startIndex):
                return(num[endIndex])
            midVal = num[midIndex]
            startVal = num[startIndex]
            endVal = num[endIndex]
            if(midVal == endVal and midVal == startVal):
                left = self.findMinInRange(num,startIndex+1,midIndex)
                right = self.findMinInRange(num,midIndex+1,endIndex)
                if(left < right):
                    return(left)
                else:
                    return(right)
                
            elif(midVal > endVal):
                return(self.findMinInRange(num,midIndex+1,endIndex))
            else:
                return(self.findMinInRange(num,startIndex+1,midIndex))
                    
                    
                
                
        
testData = [1,1]
ss= Solution()
result = ss.findMin(testData)
print(result)