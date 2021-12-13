# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        to_visit = [root]
        visited = []

        while len(to_visit) > 0:
            curr = to_visit[-1]

            if curr.left is None and curr.right is None:
                visited.append(curr.val)
                to_visit.pop()

            if curr.right is not None:
                to_visit.append(curr.right)
                curr.right = None

            if curr.left is not None:
                to_visit.append(curr.left)
                curr.left = None

        return visited


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(4)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(6)
print(Solution().postorderTraversal(root))