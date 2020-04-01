# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.pathOfBinaryTree(root)
        return self.diameter

    def pathOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_path = self.pathOfBinaryTree(root.left)
        right_path = self.pathOfBinaryTree(root.right)
        diameter = left_path + right_path

        if self.diameter < diameter:
            self.diameter = diameter

        return (left_path if left_path > right_path else right_path) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.left.right.right = TreeNode(6)
root.left.right.right.right = TreeNode(7)

print(Solution().diameterOfBinaryTree(root))
