from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        leaves_list = self.helper(root, 0)
        leaf_depth_pairs = [(leaves_list[i], leaves_list[i + 1]) for i in range(0, len(leaves_list) - 1, 2)]
        deepest = max(i[1] for i in leaf_depth_pairs)
        return sum(i[0] for i in leaf_depth_pairs if i[1] == deepest)

    def helper(self, root: TreeNode, depth: int) -> List[tuple]:
        if not root:
            return
        if not (root.left or root.right):  # checks if leaf
            return (root.val, depth)
        ans = []
        if root.left:
            ans.extend(self.helper(root.left, depth + 1))
        if root.right:
            ans.extend(self.helper(root.right, depth + 1))
        return ans
