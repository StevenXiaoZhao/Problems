# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.lowestCommonAncestorNode = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.isLowestCommonAncestorFound(root, p, q)

        return self.lowestCommonAncestorNode

    def isLowestCommonAncestorFound(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> (bool, bool):
        p_found = False
        q_found = False
        if root == p:
            p_found = True

        if root == q:
            q_found = True

        if root is None:
            return False, False

        if not(p_found and q_found) and (p.val<root.val or q.val<root.val):
            p_found1, q_found1 = self.isLowestCommonAncestorFound(root.left, p, q)
            p_found = p_found or p_found1
            q_found = q_found or q_found1

        if not (p_found and q_found) and (p.val>root.val or q.val>root.val):
            p_found1, q_found1 = self.isLowestCommonAncestorFound(root.right, p, q)
            p_found = p_found or p_found1
            q_found = q_found or q_found1

        if p_found and q_found and self.lowestCommonAncestorNode is None:
            self.lowestCommonAncestorNode = root
        return p_found, q_found

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
p = root.left
q = root.right

print(Solution().lowestCommonAncestor(root, p, q).val)