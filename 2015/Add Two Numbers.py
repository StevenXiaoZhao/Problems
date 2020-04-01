# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        more = 0
        result = None
        retail = None
        p = l1
        q = l2
        while p != None or q != None:
            pVal = p.val if p != None else 0
            qVal = q.val if q != None else 0
            val = pVal + qVal + more
            more = val //10
            val = val%10
            newNode = ListNode(val)
            if result == None:
                result = newNode
                retail = newNode
            else:
                retail.next = newNode
                retail = retail.next
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        while more >0:
            newNode = ListNode(more)
            retail.next = newNode
            retail = retail.next
            more = more//10
        return(result)
ss = Solution()
l1 = ListNode(2)
l2 = ListNode(1)
l3 = ListNode(8)
l1.next = l2
l2.next = l3

ll1 = ListNode(5)
ll2 = ListNode(6)
ll3 = ListNode(0)
ll1.next = ll2
ll2.next = ll3

result = ss.addTwoNumbers(l2,ll3)
while(result != None):
    print(result.val)
    result = result.next