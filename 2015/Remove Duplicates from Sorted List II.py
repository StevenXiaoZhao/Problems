# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        fakeHead = ListNode(0)
        fakeHead.next = head
        isDuplicate = False
        dupVal = 0
        while(fakeHead.next != None):
            if(fakeHead.next.next != None and fakeHead.next.val == fakeHead.next.next.val):
                isDuplicate = True
                dupVal = fakeHead.next.val
                fakeHead.next = fakeHead.next.next.next
            elif(isDuplicate):
                if(dupVal == fakeHead.next.val):
                    fakeHead.next = fakeHead.next.next
                else:
                    isDuplicate = False
                    break
            else:
                break
        if(fakeHead.next == None):
            return(None)
        else:
            isDuplicate = False
            p = fakeHead.next
            while(p!=None and p.next !=None):
                if(p.next.next !=None and p.next.val == p.next.next.val):
                    isDuplicate = True
                    dupVal = p.next.val
                    p.next = p.next.next.next
                elif(isDuplicate):
                    if(p.next.val == dupVal):
                        p.next = p.next.next
                    else:
                        isDuplicate = False
                        p = p.next
                else:
                    p = p.next
            return(fakeHead.next)
ss= Solution()
a = ListNode(2)
b = ListNode(4)
c = ListNode(4)
d = ListNode(4)
d.next =c
c.next = b
b.next =a

result = ss.deleteDuplicates(d)
while(result !=None):
    print(result.val)
    result = result.next
        
        