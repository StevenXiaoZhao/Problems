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
            return (self.buildSubTree(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1))

    def buildSubTree(self, inorder, in_start, in_end, postorder, post_start, post_end):
        if post_end < post_start:
            return(None)
        root = TreeNode(postorder[post_end])
        if post_end == post_start:
            return(root)
        mid = -1
        for i in range(in_start, in_end +1):
            if inorder[i] == postorder[post_end]:
                mid = i
                break
        if mid == -1:
            print('error list')
            return(None)
        leftLen = mid - in_start
        leftRoot = self.buildSubTree(inorder, in_start, mid-1, postorder, post_start, post_start + leftLen -1)
        rightRoot = self.buildSubTree(inorder, mid+1 , in_end, postorder, post_start + leftLen, post_end -1)
        root.left = leftRoot
        root.right = rightRoot
        return(root)
        
        
ss = Solution()
testData1 = [4,2,5,1,3]
testData2 = [4,5,2,3,1]
result = ss.buildTree(testData1,testData2) 
result.printTree()            
        