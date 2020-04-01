# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
    	if(l1 ==None):
    		return(l2)
    	elif(l2 == None):
    		return(l1)
    	else:
    		p_l1 = ListNode(0)
    		p_l1.next = l1
    		p_l2 = ListNode(0)
    		p_l2.next = l2
    		merged_head = ListNode(0)
    		merged_trail = ListNode(0)
    		if(l1.val <= l2.val):
    			merged_head.next = l1
    			p_l1.next = l1.next
    		else:
    			merged_head.next = l2
    			p_l2.next = l2.next

    		merged_trail.next = merged_head.next

    		while(p_l1.next != None	and p_l2.next != None) :
    			if(p_l1.next.val<=p_l2.next.val):
    				merged_trail.next.next = p_l1.next
    				merged_trail.next = p_l1.next
    				p_l1.next = p_l1.next.next
    			else:
    				merged_trail.next.next = p_l2.next
    				merged_trail.next = p_l2.next
    				p_l2.next = p_l2.next.next
    		if(p_l1.next !=None):
    			merged_trail.next.next = p_l1.next
    		else:
    			merged_trail.next.next = p_l2.next
    		return(merged_head.next)

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
result = ss.mergeTwoLists(None,None)
while result!=None:
	print(result.val)
	result = result.next
