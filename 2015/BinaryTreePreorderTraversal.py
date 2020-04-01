# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversalLog(self, root, orderList):
    	if(root == None):
    		return
    	else:
            orderList.append(root.val)
            self.preorderTraversalLog(root.left,orderList)
            self.preorderTraversalLog(root.right,orderList)
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
    	orderList = []
    	self.preorderTraversalLog(root,orderList)
    	return(orderList)



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
d.left = c
d.right = b

ss = Solution()
orderList = ss.preorderTraversal(d)
print(orderList)