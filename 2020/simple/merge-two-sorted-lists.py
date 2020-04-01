# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        head = ListNode(0)
        p = ListNode(0)
        q = ListNode(0)
        r = ListNode(0)

        p.next =l1
        q.next =l2
        r.next =head
        while p.next is not None and q.next is not None:
            if p.next.val <= q.next.val:
                r.next.next = p.next
                p.next = p.next.next
            else:
                r.next.next = q.next
                q.next = q.next.next

            r.next = r.next.next

        if p.next is None:
            r.next.next = q.next
        else:
            r.next.next = p.next

        return head.next

def buildList(a:list)->ListNode:
    head = ListNode(0)
    p = ListNode(0)
    p.next = head

    for x in a:
        p.next.next = ListNode(x)
        p.next = p.next.next

    return head.next

l1 = buildList([1,2,4])
l2 = buildList([1,3,4,5,6,7])
result = Solution().mergeTwoLists(l1, l2)
p = ListNode(0)
p.next = result
while p.next is not None:
    print(p.next.val)
    p.next = p.next.next