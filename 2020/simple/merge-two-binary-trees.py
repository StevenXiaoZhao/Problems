# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from BinaryTree import TreeNode
from BinaryTree import array2Tree
from BinaryTree import tree2List


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        if t2 is None:
            return t1
        if t1 is None:
            return t2

        t1.val += t2.val
        root = t1
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root

t1 = array2Tree([1,3,2,5])
t2 = array2Tree([2,1,3,None,4,None,7])
result = Solution().mergeTrees(t1, t2)
print(tree2List(result))