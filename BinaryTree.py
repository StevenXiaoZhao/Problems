# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def array2Tree(arr: List[int]) -> TreeNode:
    children_index = 1
    if arr is None or len(arr) == 0:
        return None
    if len(arr) == 1:
        return TreeNode(arr[0])

    root = TreeNode(arr[0])
    queue = []
    queue.append(root)
    while children_index < len(arr):
        root_node = queue[0]
        queue.remove(root_node)
        if arr[children_index] is not None:
            node = TreeNode(arr[children_index])
            root_node.left = node
            queue.append(node)

        children_index += 1
        if children_index < len(arr) and arr[children_index] is not None:
            node = TreeNode(arr[children_index])
            root_node.right = node
            queue.append(node)

        children_index += 1

    return root


def tree2List(t: TreeNode) -> List[int]:
    if t is None:
        return []
    result = []
    queue = [t]
    while len(queue) > 0:
        root =queue.pop(0)
        if root is None:
            result.append(None)
            continue

        result.append(root.val)
        if root.left is not None:
            queue.append(root.left)

        if root.right is not None:
            if root.left is None:
                queue.append(None)
            queue.append(root.right)

    return result
