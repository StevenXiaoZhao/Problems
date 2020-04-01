class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        s1_len = len(s1)
        s2_len = len(s2)
        if(s1_len != s2_len):
            return(False)
        return(isScramblePart(s1,s2, 0, s1_len-1))
    def isScramblePart(self,s1,s2,leftIndex,rightIndex):
        if(rightIndex - leftIndex <=1):
            return(True)
        leftVal = s2[leftIndex]
        midIndex = -1
        for i in range(leftIndex,rightIndex+1):
            if(leftVal == s1[i]):
                midIndex = i
                break
        if(midIndex == -1):
            return(False)
        elif(midIndex == rightIndex):
            return(self.isScramblePart(self,s1,s2,leftIndex,rightIndex-1))
        elif(midIndex == leftIndex):
            return(self.isScramblePart(self,s1,s2,leftIndex+1,rightIndex))
        else:
            
    # bug: same characters
    def isDivideCorrect(self,s1,s2,leftIndex,rightIndex, midIndex):
        leftMax = -1
        rightMin = -1
        for i in range(leftIndex, midIndex +1):
            val = s1[i]
            for j in range(leftIndex, rightIndex +1):
                if val == s2[j]:
                    if leftMax > j:
                        leftMax == j
        for i in range(rightIndex, midIndex, -1):
            val = s1[i]
            for j in range(rightIndex, leftIndex, -1):
                if j< leftMax:
                    return(False)
                elif val == s2[j]:
                    break
        return(True)
                    
        