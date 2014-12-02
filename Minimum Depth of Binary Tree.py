# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if(root == None):
            return(0)
        elif(root.left == None and root.right == None):
            return(1)
        elif(root.left != None and root.right != None):
            return(1+min(self.minDepth(root.left), self.minDepth(root.right)))
        elif(root.left == None):
            return(1+self.minDepth(root.right))
        else:
            return(1+self.minDepth(root.left))
ss= Solution()
a= TreeNode('a')
a.left = None
a.right = None

b= TreeNode('b')
b.left = None
b.right = a

e= TreeNode('e')
f= TreeNode('f')

c= TreeNode('c')
c.left = e
c.right = f

d= TreeNode('d')
d.left = c
d.right = b
result = ss.minDepth(d)
print(result)     