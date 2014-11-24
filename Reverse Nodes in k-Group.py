# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if(k<=1 or head == None):
            return(head)
        else:
            p=head
            count = 0
            while(p!=None):
                p=p.next
                count+=1
            if(count<k):
                return(head)
            fakeHead = ListNode(0)
            fakeHead.next = head
            nextHead = ListNode(0)
            nextHead.next = head
            prevTail = ListNode(0)
            prevTail.next = fakeHead
            while(nextHead.next != None):
                for i in range(k-1):
                    if(nextHead.next != None):
                        nextHead.next = nextHead.next.next
                    else:
                        return(fakeHead.next)
                if(nextHead.next == None):
                    return(fakeHead.next)
                Tail = nextHead.next
                nextHead.next = Tail.next
                Tail.next = None
                result = self.reverseList(prevTail.next.next)
                prevTail.next.next = result
                while(prevTail.next.next != None):
                    prevTail.next = prevTail.next.next
                prevTail.next.next = nextHead.next
            return(fakeHead.next)
    def reverseList(self,head):
        p = ListNode(0)
        q = ListNode(0)
        r = ListNode(0)
        p.next = head
        q.next = head.next
        r.next = head.next.next
        
        p.next.next = None
        
        while(True):
            q.next.next = p.next
            if(r.next == None):
                return(q.next)
            else:
                p.next = q.next
                q.next = r.next
                r.next = r.next.next
ss = Solution()
a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')
e = ListNode('e')
f = ListNode('f')
a.next =b
b.next =c
c.next =d
d.next =e
e.next =f

result = ss.reverseKGroup(d,2)
while(result != None):
    print(result.val)
    result = result.next
                
                        
                    