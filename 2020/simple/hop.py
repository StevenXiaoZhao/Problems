class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    A = TreeNode(0)
    B = TreeNode(0)
    A_dist = 0
    B_dist = 0
    result = -1

    def getDistance(self, root: TreeNode, A: TreeNode, B: TreeNode) -> int:
        if root is None or A is None or B is None:
            return -1

        self.A = A
        self.B = B
        A_found, B_found = self.travesalTree(root, 1)
        if A_found and B_found:
            return self.result
        else:
            return -1

    def travesalTree(self, root: TreeNode, dist:int) ->(bool, bool):
        A_found_1 = False
        A_found_2 = False
        B_found_1 = False
        B_found_2 = False

        if root.left is not None:
            (A_found_1, B_found_1) = self.travesalTree(root.left, dist+1)

        if root.right is not None:
            (A_found_2, B_found_2) = self.travesalTree(root.right, dist+1)

        A_found = A_found_1 or A_found_2
        B_found = B_found_1 or B_found_2

        if A_found and B_found and self.result == -1:
            self.result = self.A_dist + self.B_dist - dist*2
            return True, True

        if root is self.A:
            self.A_dist = dist
            A_found = True

        if root is self.B:
            self.B_dist = dist
            B_found = True

        if A_found and B_found and self.result == -1:
            self.result = self.A_dist + self.B_dist - dist*2
            return True, True

        return A_found, B_found