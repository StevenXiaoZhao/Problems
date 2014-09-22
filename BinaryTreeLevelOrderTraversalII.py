# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
    	NextFloorFlag = -1999
    	if(root == None):
    		return([])
    	numQueue =[root.val]
    	numQueue.append(NextFloorFlag)
    	rootIndex =0
    	treeQueue =[root]
    	treeIndex =0
    	while(True) :
        	if(treeIndex >= len(treeQueue)):
        		break
        	if(numQueue[rootIndex] == NextFloorFlag):
        		numQueue.append(NextFloorFlag)
        		rootIndex +=1
        	if(treeQueue[treeIndex].right!=None):
        		numQueue.append(treeQueue[treeIndex].right.val)
        		treeQueue.append(treeQueue[treeIndex].right)
        	if(treeQueue[treeIndex].left !=None):
        		numQueue.append(treeQueue[treeIndex].left.val)
        		treeQueue.append(treeQueue[treeIndex].left)
        	treeIndex +=1
        	rootIndex +=1
    	row=[]
    	result=[]
    	for x in range(len(numQueue)-1, -1, -1):
        	if(numQueue[x] == NextFloorFlag and len(row) >0):
        		result.append(row)
        		row=[]
        	elif(numQueue[x] != NextFloorFlag):
        		row.append(numQueue[x])
    	result.append(row)
    	return(result)














a= TreeNode(1)
a.left = None
a.right = None

b= TreeNode(2)
b.left = None
b.right = a

c= TreeNode(3)
c.left = None
c.right = None

d= TreeNode(4)
d.left = c
d.right = b
ss= Solution()

result = ss.levelOrderBottom(a)

print(result)

        	





        	