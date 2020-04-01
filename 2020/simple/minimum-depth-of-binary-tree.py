# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.getMinDepth(root, 0)

    def getMinDepth(self, node: TreeNode, depth: int) -> int:
        if node is None:
            return depth

        if node.left is None and node.right is None:
            return depth + 1

        left_depth = self.getMinDepth(node.left, depth + 1) if node.left is not None else float('inf')
        right_depth = self.getMinDepth(node.right, depth + 1) if node.right is not None else float('inf')

        return left_depth if left_depth < right_depth else right_depth