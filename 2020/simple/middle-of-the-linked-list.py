# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        p = ListNode(0)
        p.next = head
        while p.next is not None:
            count += 1
            p.next = p.next.next

        half = int(count/2)
        p.next = head
        while half>0:
            p.next = p.next.next
            half-=1

        return p.next
