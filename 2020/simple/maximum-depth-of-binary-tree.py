# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepths(root, 0)

    def maxDepths(self, root: TreeNode, depth:int)->int:
        if root is None:
            return depth

        left_depth = self.maxDepths(root.left, depth+1)
        right_depth = self.maxDepths(root.right, depth + 1)
        return left_depth if left_depth>=right_depth else right_depth
