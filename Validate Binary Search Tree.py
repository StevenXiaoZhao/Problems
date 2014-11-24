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
            [result, min_val,max_val] = self.isValidBSTFromRoot(root)
            return(result)
    def isValidBSTFromRoot(self, root):
            leftSub = root.left
            rightSub = root.right
            leftResult = True
            rightResult = True
            left_min = root.val
            right_max = root.val
            if(leftSub !=None):
                if(root.val <= leftSub.val):
                    return([False,None,None])
                else:
                    [leftResult,left_min,left_max] = self.isValidBSTFromRoot(leftSub)
                    if(leftResult == False or left_max >= root.val):
                        return([False,None,None])
            if(rightSub != None):
                if(root.val >= rightSub.val):
                    return([False,None,None])
                else:
                    [rightResult,right_min,right_max] = self.isValidBSTFromRoot(rightSub)
                    if(rightResult == False or right_min <= root.val):
                        return([False,None,None])
            if(leftResult and rightResult):
                return([True, left_min, right_max])
a= TreeNode(-1)
a.left = None
a.right = None

b= TreeNode(0)
b.left = a
b.right = None

c= TreeNode(1)
c.left = None
c.right = None

d= TreeNode(2)
d.left = c
d.right = b

ss = Solution()
orderList = ss.isValidBST(b)
print(orderList)
        