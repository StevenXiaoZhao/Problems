# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def printTree(self):
        if(self == None):
            return
        else:
            print(self.val)
            if(self.left != None):
                self.left.printTree()
            if(self.right != None):
                self.right.printTree()    

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if(inorder == None or inorder == []):
            return None
        elif(len(inorder) == 1):
            return TreeNode(inorder[0])
        else:
            nodeCollection = {}
            count = len(inorder)
            for i in range(count -1, -1, -1):
                val = postorder[i]
                root = None
                if(val in nodeCollection):
                    root = nodeCollection[val]
                else:
                    root = TreeNode(val)
                    nodeCollection[val] = root
                index = -1
                for j in range(len(inorder) -1, -1,-1):
                    if(inorder[j] == val):
                        index = j
                        break
                for j in range(index-1, -1, -1):
                    if((postorder[j] in nodeCollection) == False):
                        leftNode = TreeNode(postorder[j])
                        nodeCollection[postorder[j]] = leftNode
                        root.left = leftNode
                        break
                for j in range(i-1, index-1, -1):
                    if((postorder[j] in nodeCollection) == False):
                        rightNode = TreeNode(postorder[j])
                        nodeCollection[postorder[j]] = rightNode
                        root.right = rightNode
                        break
                del(inorder[index])

            return(nodeCollection[postorder[len(postorder)-1]])

ss = Solution()
testData1 = [1,2,3]
testData2 = [3,2,1]
result = ss.buildTree(testData1,testData2) 
result.printTree()            
        