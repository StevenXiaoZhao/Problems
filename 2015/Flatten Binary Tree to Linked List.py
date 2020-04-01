# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    last = TreeNode(0)
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.flattenToLeft(root)
        self.leftToRight(root)
    def flattenToLeft(self, root):
        if(root == None):
            return
        #print(root.val)
        if(self.last.left == None):
            self.last.left = root
            self.flattenToLeft(root.left)
            self.flattenToLeft(root.right)
        else:
            self.last.left.left = root
            self.last.left = root
            if(root.left != None):
                self.flattenToLeft(root.left)
            if(root.right !=None):
                self.flattenToLeft(root.right)
    def leftToRight(self, root):
        if(root == None):
            return
        else:
            root.right = root.left
            root.left = None
            self.leftToRight(root.right)

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

ss.flatten(d)
while(d!=None):
    print(d.val)
    d=d.right