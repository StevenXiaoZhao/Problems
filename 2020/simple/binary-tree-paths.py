# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []

        val = str(root.val)
        if root.left is None and root.right is None:
            return [val]
        paths = []
        if root.left is not None:
            paths.extend(self.binaryTreePaths(root.left))

        if root.right is not None:
            paths.extend(self.binaryTreePaths(root.right))

        for i in range(len(paths)):
            paths[i] = val + '->' + paths[i]

        return paths

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(Solution().binaryTreePaths(root))