"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def helper(root, depth):
            if root:
                depths = []
                for child in root.children:
                    depths.append(helper(child, depth+1))
                if len(depths) > 0:
                    return max(depths)
                else:
                    return depth
            else:
                return 0
        return helper(root, 1)
