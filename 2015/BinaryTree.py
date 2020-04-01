# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
# @param root, a tree node
# @return an integer
    def maxDepth(self, root):
        if root==None:
            return 0
        else:
            if root.left!=None:
                lmax=self.maxDepth(root.left)
            else:
                lmax=0
            if root.right!=None:
                rmax=self.maxDepth(root.right)
            else:
                rmax=0
            return max(lmax, rmax)+1

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
length = ss.maxDepth(d)
print(length)