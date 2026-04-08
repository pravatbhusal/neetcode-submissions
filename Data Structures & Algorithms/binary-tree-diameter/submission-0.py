# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # get height of left side of tree
        # get height of right side of tree
        # diameter = left_height + right_height
        # diameter may not always be from root because the longest path could be a subtree
        if root == None:
            return 0

        def get_height(node, diam):
            if node == None:
                return 0

            # get height of left and right side of subtree
            left_height = get_height(node.left, diam)
            right_height = get_height(node.right, diam)

            # update max diam encountered
            subtree_diam = left_height + right_height
            diam[0] = max(diam[0], subtree_diam)

            # return height of subtree
            return max(left_height, right_height) + 1
        
        diam = [0]
        get_height(root, diam)
        return diam[0]