# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
    	p= head
    	while(True) :
    		if(p == None or p.next == None):
    			return head
    		else:
    			if(p.next.val == p.val):
    				p.next = p.next.next
    			else:
    				p=p.next