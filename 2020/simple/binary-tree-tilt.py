# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root: TreeNode) -> int:
        self.sumNode(root)
        return self.tilt

    def sumNode(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.sumNode(root.left)
        right = self.sumNode(root.right)
        self.tilt += abs(left - right)
        return root.val + left + right
