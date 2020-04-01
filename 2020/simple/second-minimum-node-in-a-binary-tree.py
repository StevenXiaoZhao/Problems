# Definition for a binary tree node.

from BinaryTree import *

class Solution:
    def __init__(self):
        self.min_val = 0
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        self.min_val = root.val
        return self.findSecondMinimum(root)

    def findSecondMinimum(self, root: TreeNode) -> int:
        if root is None:
            return -1

        if root.val > self.min_val:
            return root.val

        left_second_min = self.findSecondMinimum(root.left)
        right_second_min = self.findSecondMinimum(root.right)

        if left_second_min == -1:
            return right_second_min
        elif right_second_min == -1:
            return left_second_min
        else:
            return left_second_min if left_second_min < right_second_min else right_second_min


test = array2Tree([2,2,2,2,2,2,2])
L =3
R =4
result = Solution().findSecondMinimumValue(test)
print(result)