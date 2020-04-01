# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        p=head
        q=head
        if(head == None):
            return(None)
        first = True
        while(p!=q or first == True):
            first = False
            if(p.next == None or q.next == None or q.next.next == None):
                return(None)
            q=q.next.next
            p=p.next
        p=head
        while(p!=q):
            q=q.next
            p=p.next
        return(p)
a= ListNode(1)
b= ListNode(2)
c= ListNode(3)
a.next=b
b.next=c
c.next=a
ss=Solution()
result = ss.detectCycle(a)
if(result!=None):
    print(result.val)
    
            
        