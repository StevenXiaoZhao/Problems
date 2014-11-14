# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        left = []
        right = []
        if(root == None):
            return([])
        else:
            left.append(root)
        result = []
        while(left !=[] or right != []):
            oneLevel = []
            while(len(left) != 0):
                curr = left.pop()
                oneLevel.append(curr.val)
                if(curr.left != None):
                    right.append(curr.left)
                if(curr.right != None):
                    right.append(curr.right)
            if(oneLevel != []):
                result.append(oneLevel)
            oneLevel = []
            while(len(right) != 0):
                curr = right.pop()
                oneLevel.append(curr.val)
                if(curr.right != None):
                    left.append(curr.right)
                if(curr.left != None):
                    left.append(curr.left)
            if(oneLevel != []):
                result.append(oneLevel)
        return(result)
ss = Solution()
a= TreeNode('a')
a.left = None
a.right = None

b= TreeNode('b')
b.left = TreeNode('e')
b.right = a

c= TreeNode('c')
c.left = None
c.right = None

d= TreeNode('d')
d.left = c
d.right = b
result = ss.zigzagLevelOrder(d)
print(result)
        