# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.isSubtree_child(s, t, False)

    def isSubtree_child(self, s: TreeNode, t: TreeNode, must_check:bool) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if must_check:
            return s.val == t.val and self.isSubtree_child(s.left, t.left, True) and self.isSubtree_child(s.right, t.right, True)

        if s.val == t.val and self.isSubtree_child(s.left, t.left, True) and self.isSubtree_child(s.right, t.right,
                                                                                                  True):
            return True

        return self.isSubtree_child(s.left, t, False) or self.isSubtree_child(s.right, t, False)
