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
            self.printTree(self.left)
            self.printTree(self.right)