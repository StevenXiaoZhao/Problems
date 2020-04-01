# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if(head == None or head.next == None):
            return(head)
        else:
            judgeVal = (head.val + head.next.val)//2
            count = 0
            leftCount = 0
            p = head
            minVal = judgeVal
            while(p!=None):
                count+=1
                if p.val <=judgeVal:
                    leftCount +=1
                if(minVal > p.val):
                    minVal = p.val
                p = p.next
            
            if(count == leftCount): #we need to choose judgeval again
                if(minVal == judgeVal):
                    return(head)
                judgeVal = (minVal + head.val)//2
                leftCount = 0
                p = head
                while(p!=None):
                    if p.val <=judgeVal:
                        leftCount +=1
                    p = p.next
            left = head
            leftRetail = head
            for i in range(leftCount-1):
                leftRetail = leftRetail.next
            right = leftRetail.next
            leftRetail.next = None
            # exchange the value of two list
            p = left
            q = right
            while(p!=None and q != None):
                if p.val <= judgeVal:
                    p = p.next
                    continue
                elif q.val > judgeVal:
                    q = q.next
                    continue
                else:
                    temp = p.val
                    p.val = q.val
                    q.val = temp
                    p = p.next
                    q = q.next
            left = self.sortList(left)
            right = self.sortList(right)
            leftRetail.next = right
            return(left)
ss = Solution()
a1 = ListNode(4)
a2 = ListNode(4)
a3 = ListNode(2)
a4 = ListNode(1)
a1.next =a2
a2.next =a3
a3.next =a4
result = ss.sortList(a3)
while(result!= None):
    print(result.val)
    result = result.next
        