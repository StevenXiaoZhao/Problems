# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        numA =1
        numB =1
        p = ListNode(0)
        p.next = headA

        while p.next is not None and p.next.next is not None:
            numA +=1
            p.next = p.next.next

        q = ListNode(0)
        q.next = headB
        while q.next is not None and q.next.next is not None:
            numB +=1
            q.next = q.next.next

        if p.next != q.next:
            return None

        # find the intersection node
        p.next = headA
        q.next = headB
        while numA-numB>0:
            numA -=1
            p.next = p.next.next

        while numA-numB<0:
            numB -=1
            q.next = q.next.next

        while p.next != q.next:
            p.next = p.next.next
            q.next = q.next.next

        return p.next
