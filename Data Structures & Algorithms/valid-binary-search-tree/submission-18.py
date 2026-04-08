# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # A child node's value is always in a range between the parent and grandparents
        # As we traverse down, we keep tightening this range
        # Solutioin: Track the subtree min/max as you traverse down
        # Start off with constraints: range min = -1001, max = 1001

        return self.helper(root, -1001, 1001)

    def helper(self, node, min, max):
        if not node:
            return True
        if node.val <= min:
            return False
        if node.val >= max:
            return False

        return self.helper(node.left, min, node.val) and self.helper(node.right, node.val, max)