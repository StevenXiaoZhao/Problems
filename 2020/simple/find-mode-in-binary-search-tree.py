# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        max_vals = self.searchMode(root)
        max_count = 0
        for val in max_vals:
            if max_vals[val]>max_count:
                max_count = max_vals[val]

        result = []
        for val in max_vals:
            if max_vals[val] == max_count:
                result.append(val)
        return result

    def searchMode(self, root: TreeNode):
        if root is None:
            return dict()

        left_max_vals = self.searchMode(root.left)
        right_max_vals = self.searchMode(root.right)

        max_vals = left_max_vals

        for val in right_max_vals:
            if val in max_vals:
                max_vals[val] += right_max_vals[val]
            else:
                max_vals[val] = right_max_vals[val]

        if root.val in max_vals:
            max_vals[root.val] += 1
        else:
            max_vals[root.val] = 1

        return max_vals


root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(2)
root.right.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.left.left = TreeNode(3)
root.left.left.left.left.left = TreeNode(3)
print(Solution().searchMode(root))
print(Solution().findMode(root))
