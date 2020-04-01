# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.minimumDifference = -1

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.getMaxMinVal(root)
        return self.minimumDifference

    def getMaxMinVal(self, root: TreeNode) -> (int, int):
        val = root.val
        max_val = val
        min_val = val
        if root.left is not None:
            left_max, left_min = self.getMaxMinVal(root.left)
            min_val = left_min
            if self.minimumDifference == -1 or val - left_max < self.minimumDifference:
                self.minimumDifference = val - left_max

        if root.right is not None:
            right_max, right_min = self.getMaxMinVal(root.right)
            max_val = right_max
            if self.minimumDifference == -1 or right_min - val < self.minimumDifference:
                self.minimumDifference = right_min - val

        return max_val, min_val

root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
print(Solution().getMinimumDifference(root))
