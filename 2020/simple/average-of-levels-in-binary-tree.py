# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from BinaryTree import TreeNode
from BinaryTree import array2Tree
from BinaryTree import tree2List


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        if root is None:
            return []
        queue = [root]
        children_queue = []
        count = 0
        level_sum = 0
        result = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is not None:
                children_queue.append(node.left)

            if node.right is not None:
                children_queue.append(node.right)
            count += 1
            level_sum += node.val

            if len(queue) == 0:
                queue = children_queue
                children_queue = []
                if count > 0:
                    result.append(level_sum / count)
                level_sum = 0
                count = 0

        return result

test = array2Tree([3,9,20,15,7])
print(Solution().averageOfLevels(test))
