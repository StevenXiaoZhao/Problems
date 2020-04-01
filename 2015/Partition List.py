# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        smaller = ListNode(0)
        bigger = ListNode(0)
        nextSmaller = ListNode(0)
        biggerBeforeNextSmaller = ListNode(0)
        fakeHead = ListNode(x-1)
        fakeHead.next = head
        smaller.next = fakeHead
        while(True):
            while(smaller.next != None and smaller.next.val < x):
                if(smaller.next.next == None or smaller.next.next.val>=x):
                    break
                else:
                    smaller.next = smaller.next.next
            if(smaller.next == None or smaller.next.next == None):
                break
            else:
                bigger.next = smaller.next.next
            
            biggerBeforeNextSmaller.next = bigger.next
            while(biggerBeforeNextSmaller.next !=None and biggerBeforeNextSmaller.next.val >=x):
                if(biggerBeforeNextSmaller.next.next == None or biggerBeforeNextSmaller.next.next.val <x):
                    break
                else:
                    biggerBeforeNextSmaller.next = biggerBeforeNextSmaller.next.next
            if(biggerBeforeNextSmaller.next == None or biggerBeforeNextSmaller.next.next == None):
                break
            else:
                nextSmaller.next = biggerBeforeNextSmaller.next.next
            smaller.next.next = nextSmaller.next
            biggerBeforeNextSmaller.next.next = nextSmaller.next.next
            nextSmaller.next.next = bigger.next
        return(fakeHead.next)
def ConstructList(data):
    root = ListNode(data[0])
    prev = ListNode(data[0])
    prev.next = root
    first =True
    for x in data:
        if(first):
            first= False
            continue
        tt = ListNode(x)
        prev.next.next =tt
        prev.next = tt
    return(root)
        
        
ss =Solution()
testData = ConstructList([1,4,3,2,5,2])
result = ss.partition(testData,3)

curr = ListNode(0)
curr.next = result
while(curr.next != None):
    print(curr.next.val)
    curr.next = curr.next.next

        