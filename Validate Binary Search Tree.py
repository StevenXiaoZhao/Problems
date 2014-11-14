# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if(root == None):
            return(True)
        else:
            return(self.isValidBSTFromRoot(root,root.val))
    def isValidBSTFromRoot(self, root, rootParentVal):
            leftSub = root.left
            rightSub = root.right
            leftResult = True
            rightResult = True
            if(leftSub !=None):
                if(root.val <= leftSub.val):
                    return(False)
                else:
                    leftResult = self.isValidBSTFromRoot(leftSub,root.val)
            if(rightSub != None):
                if(root.val >= rightSub.val or rightSub.val>=rootParentVal):
                    return(False)
                else:
                    rightResult = self.isValidBSTFromRoot(rightSub,root.val)
            if(leftResult and rightResult):
                return(True)
            return(False)
a= TreeNode(2)
a.left = None
a.right = None

b= TreeNode(3)
b.left = a
b.right = None

c= TreeNode(1)
c.left = None
c.right = None

d= TreeNode(2)
d.left = c
d.right = b

ss = Solution()
orderList = ss.isValidBST(d)
print(orderList)
        