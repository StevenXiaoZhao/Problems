# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		queueRoot = TreeNode(0) 
		head = TreeNode(0)
		level =0
		queueRoot.next = root
		head.next = root
		while(True) :
			self.connectOneLine(queueRoot,head,level)
			level+=1
			if(queueRoot.next == None):
				break
	
	def connectOneLine(self, queueRoot, head, level):
		levelCount = 2**level
		while(True):
			if(head.next == None or queueRoot.next == None):
				break
			if(queueRoot.next.left != None):
				head.next.next = queueRoot.next.left
				head.next = head.next.next
			if(queueRoot.next.right != None):
				head.next.next = queueRoot.next.right
				head.next = head.next.next
			if(levelCount == 1):
				temp = queueRoot.next
				queueRoot.next = queueRoot.next.next
				temp.next = None
				break
			else:
				queueRoot.next = queueRoot.next.next
				levelCount -=1
		return


a= TreeNode('a')
a.left = None
a.right = None

b= TreeNode('b')
b.left = None
b.right = None

c= TreeNode('c')
c.left = None
c.right = None

d= TreeNode('d')
d.left = a
d.right = b

e= TreeNode('e')
e.left = c

f= TreeNode('f')
f.left = d
f.right = e

ss= Solution()
ss.connect(f)
print(d.next.val)
print(b.next.val)
print(a.next.val)
print(f.next)