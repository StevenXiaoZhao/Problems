# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        nodeCount = 0
        p = head
        while p!=None:
            nodeCount +=1
            p = p.next
        if nodeCount == 0:
            return(None)
        k = k%nodeCount
        if k ==0:
            return(head)
        else:
            p = head
            for i in range(nodeCount - k -1):
                p = p.next
            nextHead = p.next
            p.next = None
            q= nextHead
            while(q.next != None):
                q = q.next
            q.next = head
            return(nextHead)

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
ss = Solution()
result = ss.rotateRight(l4,3)
while(result!=None):
    print(result.val)
    result = result.next
                
        