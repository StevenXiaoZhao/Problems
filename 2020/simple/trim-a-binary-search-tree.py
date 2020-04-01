# Definition for a binary tree node.

from BinaryTree import *

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return root

        left = self.trimBST(root.left, L, R)
        right = self.trimBST(root.right, L, R)
        if L <= root.val <= R:
            root.left = left
            root.right = right
            return root
        else:
            if left is not None:
                return left

            if right is not None:
                return right

            return None

test = array2Tree([2,1,3])
L =3
R =4
result = Solution().trimBST(test, L, R)
print(tree2List(result))