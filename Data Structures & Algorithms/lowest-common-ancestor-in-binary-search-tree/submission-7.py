# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST is sorted by left (smallest) and right (largest)
        # assume p < q, then p >= LCP <= q because the tree is BST
        # LCA means the lowest level which the above condition is true

        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                # cur too small, go right (larger)
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                # cur too large, go left (smaller)
                cur = cur.left
            else:
                # found node between p and q (LCA)
                return cur




    
        