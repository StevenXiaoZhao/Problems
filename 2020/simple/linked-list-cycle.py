# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p = ListNode(0)
        p.next = head
        q = ListNode(0)
        q.next = head.next if head is not None else None
        while p.next is not None and q.next is not None:
            if p.next == q.next:
                return True

            p.next = p.next.next
            q.next = q.next.next
            if q.next is not None:
                q.next = q.next.next

        return False
