# Definition for singly-linked list.
class ListNode:
	 def __init__(self, x):
		  self.val = x
		  self.next = None

class Solution:
	# @param head, a ListNode
	# @return a boolean
	def hasCycle(self, head):
		while(True):
			if(head == None):
			  return(False)
			elif(head.val == 2147483648):
				return(True)
			else:
				head.val = 2147483648
				head = head.next


a=ListNode(1)
b=ListNode(2)
c=ListNode(3)

head = ListNode(0)
head.next =a
a.next =b
b.next =c
c.next =a

ss = Solution()
result = ss.hasCycle(head)
print(result)
print(c.val)