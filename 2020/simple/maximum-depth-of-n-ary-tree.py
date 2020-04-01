
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        elif root.children is Node:
            return 1

        depth = 0
        for child in root.children:
            child_depth = self.maxDepth(child)
            if child_depth > depth:
                depth = child_depth

        return depth + 1