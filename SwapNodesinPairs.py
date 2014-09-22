# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        first = ListNode(0)
        second = ListNode(0)
        root = ListNode(0)
        if(head == None):
        	return None

        first.next = head
        second.next = head.next
        if(head.next != None):
        	root.next = head.next
        else:
        	return(head)

        while(first.next != None and second.next != None):
        	first.next.next = second.next.next
        	second.next.next = first.next
        	#move forward
        	second.next = first.next.next
        	if(second.next == None or second.next.next == None):
        		break
        	first.next.next = second.next.next
        	first.next = second.next
        	second.next = second.next.next
        return(root.next)

def BuildList(list):
	a = ListNode(list[0])
	b = ListNode(0)
	b.next =a

	list_len = len(list)
	for x in range(1,list_len):
		c = ListNode(list[x])
		b.next.next =c
		b.next =c
	return(a)

ss= Solution()
result = ss.swapPairs(BuildList([1,2,3]))
while result!=None:
	print(result.val)
	result = result.next
