# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        A_len = 0
        p = headA
        while(p!=None):
            p = p.next
            A_len +=1
        B_len = 0
        p = headB
        while(p!=None):
            p = p.next
            B_len +=1
        
        longer = headA
        longer_len = A_len
        shorter = headB
        shorter_len = B_len
        if(B_len > A_len):
            longer = headB
            shorter = headA
            longer_len = B_len
            shorter_len = A_len
        for i in range(shorter_len, longer_len):
            longer = longer.next
        for i in range(shorter_len):
            if(shorter == longer):
                return(shorter)
            else:
                shorter = shorter.next
                longer = longer.next
        return(None)

a1 = ListNode('a1')
a2 = ListNode('a2')
b1 = ListNode('b1')
b2 = ListNode('b2')
b3 = ListNode('b3')
c1 = ListNode('c1')
c2 = ListNode('c2')
c3 = ListNode('c3')

c1.next =c2
c2.next =c3

a1.next =a2
a2.next =c1

b3.next = c1

ss = Solution()
result = ss.getIntersectionNode(b1,a1)

print(result.val)