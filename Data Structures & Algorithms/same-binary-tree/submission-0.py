# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not self.check_same(p, q):
            return False
        if not p and not q:
            return True

        # DFS on both trees at the same time
        # if anything doesn't match, short-circuit and return False
        left = self.isSameTree(p.left, q.left)
        if not left:
            return False
        right = self.isSameTree(p.right, q.right)
        if not right:
            return False
        return True

    # helper to check if p and q node are the same 
    def check_same(self, p, q):
        print(p, q)
        if p and q and p.val == q.val:
            return True
        if p and q and p.left and q.left:
            return True
        if p and q and q.right and p.right:
            return True
        if not p and not q:
            return True
        return False
        