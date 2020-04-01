# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from BinaryTree import TreeNode
from BinaryTree import array2Tree

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if root.val == val:
            return root

        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)
        return left if left is not None else right

test = array2Tree([4,2,7,1,3])
print(Solution().searchBST(test, 3).val)