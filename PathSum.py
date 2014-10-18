# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if(root == None):
            return(False)
        else:
            leftVal = sum - root.val
            if(root.left == None and root.right == None and leftVal == 0):
                return(True)
            else:
                return(self.hasPathSum(root.left,leftVal) or self.hasPathSum(root.right,leftVal))

ss= Solution()
a= TreeNode(1)
a.left = None
a.right = None

b= TreeNode(2)
b.left = None
#b.right = a

c= TreeNode(3)
c.left = b
c.right = a

d= TreeNode(4)
d.left = c

result = ss.hasPathSum(d,9)
print(result)
        