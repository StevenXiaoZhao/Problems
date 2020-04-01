# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        num_set = set()
        self.traversalTree(root, num_set)
        for num in num_set:
            if k-num in num_set and num != k-num:
                return True

        return False

    def traversalTree(self, node: TreeNode, num_set: set):
        if node is not None:
            num_set.add(node.val)
            self.traversalTree(node.left, num_set)
            self.traversalTree(node.right, num_set)

