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
            if self.left != None:
                self.left.printTree()
            if self.right !=None:
                self.right.printTree()
class Solution:
    # @param inorder, a list of integers
    # @param preorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if(inorder == None or inorder == []):
            return None
        elif(len(inorder) == 1):
            return TreeNode(inorder[0])
        else:
            return (self.buildSubTree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1))

    def buildSubTree(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_end < pre_start:
            return(None)
        root = TreeNode(preorder[pre_start])
        if pre_end == pre_start:
            return(root)
        mid = -1
        for i in range(in_start, in_end +1):
            if inorder[i] == preorder[pre_start]:
                mid = i
                break
        if mid == -1:
            print('error list')
            return(None)
        leftLen = mid - in_start
        leftRoot = self.buildSubTree(preorder, pre_start + 1, pre_start + leftLen, inorder, in_start, mid-1)
        rightRoot = self.buildSubTree(preorder, pre_start + leftLen + 1, pre_end, inorder, mid+1 , in_end)
        root.left = leftRoot
        root.right = rightRoot
        return(root)
        
        
ss = Solution()
testData1 = [1,2,4,5,3]
testData2 = [4,2,5,1,3]
result = ss.buildTree(testData1,testData2) 
result.printTree()