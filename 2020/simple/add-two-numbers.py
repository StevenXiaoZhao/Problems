# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = 0
        p = ListNode(0)
        p.next = l1
        q = ListNode(0)
        q.next = l2
        result = ListNode(0)
        root = ListNode(0)
        result.next = root
        while p.next is not None or q.next is not None:
            l1_value = 0
            if p.next is not None:
                l1_value = p.next.val
                p.next = p.next.next

            l2_value = 0
            if q.next is not None:
                l2_value = q.next.val
                q.next = q.next.next

            value = left + l1_value + l2_value
            left = int(value / 10)
            curr_value = value % 10
            result.next.next = ListNode(curr_value)
            result.next = result.next.next

        if left > 0:
            result.next.next = ListNode(left)

        return root.next
