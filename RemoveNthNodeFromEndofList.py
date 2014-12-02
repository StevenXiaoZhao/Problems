# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        first = ListNode(1)
        second = ListNode(1)
        if(head == None or n == 0):
            return(head)
        first.next = head.next
        second.next = head
        for number in range(0, n-1):
            first.next = first.next.next
        if(first.next == None):
            return(head.next)
        else:
            first.next = first.next.next
            while(first.next != None):
                first.next = first.next.next
                second.next = second.next.next
            second.next.next=second.next.next.next
            return(head)
        
a = ListNode(1)

b = ListNode(2)
b.next = a
c = ListNode(3)
c.next = b
d = ListNode(4)
d.next = c
e = ListNode(5)
e.next = d

ss= Solution()
result = ss.removeNthFromEnd(e,0)
while(result!=None):
    print(result.val)
    result = result.next
        