# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Smallest node is on the very left of BST
        # Solution: Traverse to the smallest first, then traverse back up until k
        # To do this, store all nodes till k with inorder traversal
        # This is because the left traversal will visit the smallest node
        # So the inorder check occurs after smallest node has already been visited

        nodes = []
        def helper(node):
            if not node:
                return
            if len(nodes) == k:
                # already have k nodes, short-circuit
                return
            
            helper(node.left)
            nodes.append(node.val)
            helper(node.right)
        
        helper(root)
        return nodes[k - 1]
        
            
        