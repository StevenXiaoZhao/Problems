# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        curr = root
        visitStack =[root]
        printStack =[]
        while(len(visitStack)>0 and curr != None):
            while(curr.left != None):
                visitStack.append(curr.left)
                curr.left = None
                curr = visitStack[-1]
                
            curr = visitStack[-1]
            if(curr.right == None):
                printStack.append(curr.val)
                visitStack.pop()
            else:
                visitStack.append(curr.right)
                curr.right = None
                curr = visitStack[-1]
        return(printStack)

ss= Solution()
a= TreeNode('a')
a.left = None
a.right = None

b= TreeNode('b')
b.left = None
b.right = a

c= TreeNode('c')
c.left = b
c.right = None

d= TreeNode('d')
d.left = c
#d.right = b
result = ss.postorderTraversal(d)
print(result)