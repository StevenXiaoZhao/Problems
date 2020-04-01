# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = ListNode(0)
        p.next = head
        q = ListNode(0)
        if p.next is not None:
            q.next = p.next.next
        while p.next is not None and q.next is not None:

            if q.next.val == p.next.val:
                p.next.next = q.next.next
            else:
                p.next = q.next

            q.next = q.next.next
        return head

def constructList(data: List)->ListNode:
    if data is None:
        return data
    head = ListNode(0)
    p= ListNode(0)
    p.next = head
    for x in data:
        p.next.next = ListNode(x)
        p.next = p.next.next

    return head.next

def printList(head: ListNode):
    p = ListNode(0)
    p.next = head
    while p.next is not None:
        print(p.next.val)
        p.next = p.next.next

head = constructList([1,1,1,1,2,3,3])
result = Solution().deleteDuplicates(None)
printList(result)
