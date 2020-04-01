# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_count = 1

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longestUnivaluePath2(root)
        return self.max_count-1

    def longestUnivaluePath2(self, root: TreeNode) -> int:
        if root is None:
            return 0

        count1 = self.longestUnivaluePath2(root.left)
        count2 = self.longestUnivaluePath2(root.right)

        if root.left is not None:
            if root.val == root.left.val:
                count1 += 1
            else:
                if count1 > self.max_count:
                    self.max_count = count1

                count1 = 0

        if root.right is not None:
            if root.val == root.right.val:
                count2 += 1
            else:
                if count2 > self.max_count:
                    self.max_count = count2

                count2 = 0

        # count 是包含本节点在内的最长路径
        if count1 > 0 and count2 > 0:  # 左右值都等于本节点
            count = count1 + count2 - 1
            with_root_count = count1 if count1>count2 else count2
        elif count1 + count2 == 0:  # 左右都不等于本节点
            count = 1
            with_root_count = 1
        else:  # 左右有一方等于本节点
            count = count1 if count1 > 0 else count2
            with_root_count = count

        if count > self.max_count:
            self.max_count = count

        return with_root_count

root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(5)

print(Solution().longestUnivaluePath(root))