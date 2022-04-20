# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_diff = 9999

    def minDiffInBST(self, root: TreeNode) -> int:
        self.minMaxInBST(root)
        return self.min_diff

    def minMaxInBST(self, root: TreeNode) -> (int, int):
        min_in_BST = root.val
        max_in_BST = root.val
        if root.right is not None:
            right_min_in_BST,  right_max_in_BST= self.minMaxInBST(root.right)
            diff = abs(right_min_in_BST-root.val)
            if diff < self.min_diff:
                self.min_diff = diff

            max_in_BST = right_max_in_BST

        if root.left is not None:
            left_min_in_BST,  left_max_in_BST = self.minMaxInBST(root.left)
            diff = abs(left_max_in_BST - root.val)
            if diff < self.min_diff:
                self.min_diff = diff

            min_in_BST = left_min_in_BST

        return  min_in_BST, max_in_BST
