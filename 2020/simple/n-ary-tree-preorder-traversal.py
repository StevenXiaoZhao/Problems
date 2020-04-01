
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        node_stack = []
        if root is None:
            return result
        node_stack.append(root)
        while len(node_stack)>0:
            node = node_stack.pop()
            result.append(node.val)
            if node.children is not None:
                count = len(node.children)
                for i in range(count):
                    node_stack.append(node.children[count-1-i])

        return result
