# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    """
    Good = if all nodes above it are less than or equal to that node.
    
    Solution: Store the max seen num at each subtree. And if the node is >= than the
    max seen num, then it is good.
    """

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.helper(root, root.val)

    def helper(self, root: TreeNode, max: int) -> int:
        if not root:
            return 0

        good = 0
        if root.val >= max:
            # good node
            max = root.val
            good = 1

        l_goods = self.helper(root.left, max)
        r_goods = self.helper(root.right, max)
        return good + l_goods + r_goods