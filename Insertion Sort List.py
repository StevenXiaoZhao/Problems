# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if(head == None):
            return(None)
        else:
            p = head
            fakeHead = ListNode(0)
            fakeHead.next = head
            while(p!= None and p.next != None):
                if(p.next.val >= p.val):
                    p=p.next
                else:
                    q = p.next
                    p.next = q.next
                    q.next = None
                    self.Insert(fakeHead, q)
            return(fakeHead.next)
    def Insert(self, fakeHead, q):
        if(q.val< fakeHead.next.val):
            q.next = fakeHead.next
            fakeHead.next = q
        else:
            p = fakeHead.next
            while(p.next !=None):
                if(p.next.val> q.val):
                    q.next = p.next
                    p.next = q
                    return()
                else:
                    p = p.next
            p.next = q
            q.next = None
ss = Solution()
a= ListNode(3)
b= ListNode(1)
c= ListNode(2)
d= ListNode(4)
b.next =a
c.next =b
d.next =c

result = ss.insertionSortList(d)

while(result!=None):
    print(result.val)
    result = result.next
                
        