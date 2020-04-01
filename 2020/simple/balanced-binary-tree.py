# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    is_balance = True
    def isBalanced(self, root: TreeNode) -> bool:
        self.getDepth(root, 0)
        return self.is_balance

    def getDepth(self, node: TreeNode, depth:int) -> int:
        if node is None:
            return depth
        else:
            left_depth = self.getDepth(node.left, depth+1)
            right_depth = self.getDepth(node.right, depth+1)

            if abs(left_depth-right_depth)>1:
                self.is_balance = False
                return depth

            return left_depth if left_depth >= right_depth else right_depth
