# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.sumOfLeftLeavesWithDirect(root, False)

    def sumOfLeftLeavesWithDirect(self, root: TreeNode, is_left: bool) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            if is_left:
                return root.val
            else:
                return 0
        return self.sumOfLeftLeavesWithDirect(root.left, True) + self.sumOfLeftLeavesWithDirect(root.right, False)
