# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.SUM = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.SUM = sum
        return self.pathCount(root, [0])

    def pathCount(self, root: TreeNode, paths:List[int]) -> int:
        if root is None:
            return 0
        count = 0
        for path in paths:
            if path + root.val == self.SUM:
                count+=1

        for i in range(len(paths)):
            paths[i] += root.val

        paths.append(0)

        count += self.pathCount(root.left, paths)
        count += self.pathCount(root.right, paths)

        return count


root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(3)
print(Solution().pathSum(root, 3))
