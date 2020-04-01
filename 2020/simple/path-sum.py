# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    sum = 0
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.sum = sum
        if root is None:
            return sum == 0
        return self.isPathSum(root, 0)

    def isPathSum(self, node: TreeNode, val:int)->bool:
        if node is None:
            return False

        val = val+node.val
        if node.left is None and node.right is None:
            return val == self.sum

        return self.isPathSum(node.left, val) or self.isPathSum(node.right, val)
