# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        p = ListNode(0)
        p.next = head

        while p.next is not None and p.next.val == val:
            p.next = p.next.next

        q = ListNode(0)
        q.next = p.next
        while q.next is not None and q.next.next is not None:
            if q.next.next.val == val:
                q.next.next = q.next.next.next

            q.next = q.next.next

        return p.next

