# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.depth(root, 1)

    # simple DFS and keep track of longest depth, O(N) time and space
    def depth(self, node: Optional[TreeNode], max_depth: int) -> int:
        if not node:
            return max_depth
        left = self.depth(node.left, max_depth + 1) if node.left else max_depth
        right = self.depth(node.right, max_depth + 1) if node.right else max_depth
        return max(left, right)