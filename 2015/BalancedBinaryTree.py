# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
    	if(root == None):
    		return(True)
    	else:
    		is_left_balance = self.isBalanced(root.left)
    		if(is_left_balance):
    			is_right_balance = self.isBalanced(root.right)
    			if(is_right_balance and abs(self.GetTreeLength(root.left) - self.GetTreeLength(root.right))<=1):
    				return(True)
    	return(False)


    def GetTreeLength(self, root):
    	if(root == None):
    		return(0)
    	else:
    		return max(self.GetTreeLength(root.left),self.GetTreeLength(root.right))+1

a= TreeNode('a')
a.left = None
a.right = None

b= TreeNode('b')
b.left = None
b.right = a

c= TreeNode('c')
c.left = None
c.right = None

d= TreeNode('d')
#d.left = c
d.right = b

ss = Solution()
print(ss.isBalanced(d))        