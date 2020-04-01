# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        mid = int(len(nums)/2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTWithIndex(nums, 0, mid-1)
        root.right = self.sortedArrayToBSTWithIndex(nums, mid+1, len(nums)-1)
        return root

    def sortedArrayToBSTWithIndex(self, nums: List[int], s_i, e_i) -> TreeNode:
        if s_i > e_i:
            return None
        mid = int((s_i+e_i)/2)
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTWithIndex(nums, s_i, mid - 1)
        node.right = self.sortedArrayToBSTWithIndex(nums, mid + 1, e_i)
        return node