# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            # both null
            return True
        if not p or not q or p.val != q.val:
            # values don't match
            return False
        
        # DFS both trees at same time
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)