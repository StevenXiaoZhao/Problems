# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visited = []
        if root is None:
            return []

        to_visit = [root]
        while root.left is not None:
            root = root.left
            to_visit.append(root)

        while len(to_visit) > 0:
            curr = to_visit[len(to_visit)-1]
            to_visit.pop()
            # visit root
            visited.append(curr.val)

            if curr.right is not None:
                root = curr.right
                to_visit.append(root)
                while root.left is not None:
                    root = root.left
                    to_visit.append(root)

        return visited


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(4)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(6)
print(Solution().inorderTraversal(root))
