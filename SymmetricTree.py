# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if(p == None and q == None):
        	return True
        elif(p != None and q != None):
        	if(p.val == q.val):
        		return self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left)
        	else:
        		return False
        else:
        	return False
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
    	if(root == None):
    		return(True)
    	else:
    		return self.isSameTree(root.left,root.right)







a= TreeNode('a')
a.left = None
a.right = None

b= TreeNode('b')
b.left = a
b.right = None

e= TreeNode('a')
e.left = None
e.right = None

c= TreeNode('b')
c.left = None
c.right = e

d= TreeNode('d')
d.left = c
d.right = b

ss= Solution();

print(ss.isSymmetric(d))