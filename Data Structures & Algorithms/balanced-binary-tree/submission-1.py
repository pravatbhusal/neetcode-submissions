# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # at each traversal when we encounter leaf node start counting height

        if root == None:
            return True

        balanced = True
        def helper(node):
            if node == None:
                return 0
            left_height = helper(node.left)
            right_height = helper(node.right)
            height_diff = abs(left_height - right_height)
            if height_diff > 1:
                nonlocal balanced
                balanced = False
            return 1 + max(left_height, right_height)

        helper(root)
        return balanced