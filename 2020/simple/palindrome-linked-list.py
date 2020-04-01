# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        node_count = 0
        p = ListNode(0)
        p.next = head
        while p.next is not None:
            node_count += 1
            p.next = p.next.next

        half_count = int(node_count/2)
        p.next = head

        for x in range(half_count):
            p.next = p.next.next

        q = ListNode(0)
        t = ListNode(0)
        q.next = p.next.next
        p.next.next = None

        while p.next is not None and q.next is not None:

            t.next = q.next.next
            q.next.next = p.next
            p.next = q.next
            q.next = t.next

        q.next = head
        while p.next is not None:
            if q.next.val == p.next.val:
                q.next = q.next.next
                p.next = p.next.next
            else:
                return False

        return True

def constructNode(array: list) -> ListNode:
    if array is None or len(array) == 0:
        return None
    head = ListNode(array[0])
    p = ListNode(0)
    p.next = head
    for x in array:
        node = ListNode(x)
        p.next.next = node
        p.next = p.next.next

    return head.next


listNode = constructNode([])
print(Solution().isPalindrome(listNode))