# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if(root == None):
            return([])
        queue = [root]
        lastLevelCount = 1
        currLevelCount = 0
        result=[]
        while(len(queue) > 0):
            level =[]
            for i in range(0, lastLevelCount):
                level.append(queue[0].val)
                if(queue[0].left != None):
                    queue.append(queue[0].left)
                    currLevelCount += 1
                if(queue[0].right != None):
                    queue.append(queue[0].right)
                    currLevelCount += 1
                del(queue[0])
            result.append(level)
            lastLevelCount = currLevelCount
            currLevelCount = 0
        return(result)

ss= Solution()
a= TreeNode('a')
a.left = None
a.right = None

b= TreeNode('b')
b.left = None
#b.right = a

c= TreeNode('c')
c.left = b
c.right = a

d= TreeNode('d')
d.left = c

result = ss.levelOrder(a)
print(result)
                
            
        
        