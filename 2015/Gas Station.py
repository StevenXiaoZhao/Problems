class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if(gas == None):
            return(-1)        
        left = [x-y for x, y in zip(gas,cost)]
        count = len(gas)
        start_index = -1
        i=0
        while(i< count*2):
            index = i%count
            nextIndex = (i+1)%count
            if(i > count and start_index < index):
                break
            elif(left[index] <0 and left[nextIndex]>=0):
                start_index = -1
            else:
                if(left[index] >0 and start_index == -1 or left[index]==0 and i<count):
                    start_index = index
                if(nextIndex != index):
                    left[nextIndex] += left[index]
                    left[index] = 0
            i+=1
        return(start_index)
ss = Solution()
result = ss.canCompleteCircuit([6,0,1,3,2], [4,5,2,5,5])
print(result)
                    
                
                    