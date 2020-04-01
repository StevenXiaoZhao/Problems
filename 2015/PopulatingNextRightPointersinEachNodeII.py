# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if(root == None):
            return(root)
        queue=[root,None]
        while(len(queue) !=0):
            head = queue[0]
            del(queue[0])
            if(head == None):
                if(len(queue) == 0):
                    break
                queue.append(None)
                continue
            else:
                head.next = queue[0]
                if(head.left != None):
                    queue.append(head.left)
                if(head.right != None):
                    queue.append(head.right)
                
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
ss.connect(d)
print(f.next.val)        