# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if(head == None):
            return
        head_length = 0
        p = head
        while p is not None:
            p = p.next
            head_length +=1
        if(head_length == 1):
            return
        p = head
        for i in range((head_length+1)//2-1):
            p = p.next
        nextHead = p.next
        p.next = None
        nextHead = self.reverseList(nextHead)
        p1 = head
        p2 = head.next
        q1 = nextHead
        q2 = nextHead.next
        while(q2 != None):
            p1.next =q1
            q1.next =p2
            p1 = p2
            p2 = p1.next
            q1 = q2
            q2 = q1.next
        p1.next =q1
        q1.next =p2
        return(head)
    def reverseList(self, head):
        prevNode = None
        currNode = head
        nextNode = head.next
        while(nextNode != None):
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            nextNode = currNode.next
        currNode.next = prevNode
        return(currNode)

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

ss = Solution()
result = ss.reorderList(l5)
while(result!=None):
    print(result.val)
    result = result.next