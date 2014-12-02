class MinStack:
    data = [0]*1000
    minVal = 0
    count = 0
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if(self.count >= len(self.data)):
            self.data += [0]*1000
        self.data[self.count] = x
        if self.count == 0 :
            self.minVal = x
        elif self.minVal> x:
            self.minVal = x
        self.count +=1

    # @return nothing
    def pop(self):
        if(self.count>0):
            curr = self.data[self.count-1]

            if(curr==self.minVal):
                if(self.count>1):
                    self.minVal = min(self.data[0:self.count-1])
            self.count -=1

    # @return an integer
    def top(self):
        if(self.count>0):
            return(self.data[self.count-1])

    # @return an integer
    def getMin(self):
        return(self.minVal)

ms = MinStack()

for i in range(10000, 0, -1):
    ms.push(i)

print(ms.top())
print(ms.getMin())
ms.pop()
print(ms.top())
print(ms.getMin())
