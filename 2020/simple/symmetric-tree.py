# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSameTree(root.left, root.right)


    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            return p is None and q is None

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.right) and self.isSameTree(p.right,q.left)
