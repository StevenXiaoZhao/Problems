# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result

        temp = [root, None]
        data = []
        while len(temp) > 0:
            node = temp.pop(0)
            if node is None:
                result.insert(0, data)
                data = []
                if len(temp) > 0:
                    temp.append(None)
            else:
                data.append(node.val)
                if node.left is not None:
                    temp.append(node.left)
                    data.append(node.left.val)

                if node.right is not None:
                    temp.append(node.right)
                    data.append(node.right.val)

        return result
