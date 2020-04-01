# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        num = 0
        p = head
        copy = []
        hashTable = {}
        while(p!=None):
            copy.append(RandomListNode(p.label))
            hashTable[p] = num
            num +=1
            p = p.next
        for i in range(1, num):
            copy[i-1].next = copy[i]
        p = head
        i=0
        while(p!=None):
            if(p.random != None):
                point = hashTable[p.random]
                copy[i].random = copy[point]
            i +=1
            p = p.next
        if(num>0):
            return(copy[0])
        else:
            return(None)

ss = Solution()
a= RandomListNode('a')
b = RandomListNode('b')
c = RandomListNode('c')
a.next =b
b.next =c
b.random =a
c.random =a
a.random =c

result = ss.copyRandomList(a)
while(result!=None):
    randomVal = ''
    if(result.random != None):
        randomVal = result.random.label
    print(result.label+':'+randomVal)
    result = result.next
            
            