# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        fakeHead = ListNode(0)
        fakeHead.next = head
        if(m==n or head == None):
            return(head)
        leftTrail = ListNode(0)
        rightHead = ListNode(0)
        leftTrail.next = fakeHead
        for i in range(m-1):
            leftTrail.next = leftTrail.next.next
        reverseHead = ListNode(0)
        reverseHead.next = leftTrail.next.next
        leftTrail.next.next = None
        rightHead.next = reverseHead.next
        for i in range(m, n):
            rightHead.next = rightHead.next.next
        reverseTrail = ListNode(0)
        reverseTrail.next = rightHead.next
        rightHead.next = rightHead.next.next
        reverseTrail.next.next = None
        prev = reverseHead.next
        curr = prev.next
        nex = curr.next
        
        while(True):
            curr.next = prev
            prev = curr
            curr = nex
            if(nex == None):
                break
            nex = nex.next
        leftTrail.next.next = reverseTrail.next
        reverseHead.next.next = rightHead.next
        return(fakeHead.next)
def constructList(data):
    head = ListNode(data[0])
    prev = head
    for x in range(1, len(data)):
        c = ListNode(data[x])
        prev.next = c
        prev = c
    return(head)
test = constructList([1,2,3,4,5,6])
ss= Solution()
result = ss.reverseBetween(test, 2, 6)
while(result != None):
    print(result.val)
    result = result.next