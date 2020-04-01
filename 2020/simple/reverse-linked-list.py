# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        p = ListNode(0)
        q = ListNode(0)
        r = ListNode(0)
        p.next = head
        q.next = head.next
        p.next.next = None
        while p.next is not None and q.next is not None:
            r.next = q.next.next
            q.next.next=p.next
            p.next = q.next
            q.next = r.next

        return p.next