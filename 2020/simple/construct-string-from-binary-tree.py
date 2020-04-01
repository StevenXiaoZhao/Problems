# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from BinaryTree import TreeNode
from BinaryTree import array2Tree

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ''
        result = str(t.val)
        if t.left is None and t.right is not None:
            result = result + '()(' + self.tree2str(t.right) +')'
        if t.left is not None and t.right is not None:
            result = result + '('+self.tree2str(t.left)+')(' + self.tree2str(t.right) + ')'
        if t.left is not None and t.right is None:
            result = result + '(' + self.tree2str(t.left) + ')'
            return result

        return result

test = array2Tree([1,2,3,None,4])
print(Solution().tree2str(test))