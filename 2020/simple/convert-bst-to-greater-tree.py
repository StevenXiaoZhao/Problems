# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.add(root, 0)
        return root

    def add(self, root:TreeNode, parent_val:int) -> int:
        if root is None:
            return parent_val

        right_val = self.add(root.right, parent_val)
        root.val += right_val
        return self.add(root.left, root.val)

root = TreeNode(5)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(13)
root.right.left = TreeNode(8)
root.right.right = TreeNode(14)

result = Solution().convertBST(root)


