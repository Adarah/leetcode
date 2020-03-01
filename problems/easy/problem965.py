# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.helper(root, root.val)
    def helper(self, root: TreeNode, val: int) -> bool:
        if not root:
            return True
        if root.val == val:
            return self.helper(root.left, val) and self.helper(root.right, val)
        else:
            return False
