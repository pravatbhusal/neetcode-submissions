# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Path can only connect its left subtree, up to its parent, and down to the right subtree. It cannot visit the
same node twice.

Post-order traversal checking:
We can do a post-order traversal where we sum the max value from the left subtree
and the max value from the right subtree. Then add up the left + parent + right.

Kadane's algorithm:
How do we know when to stop traversing a path? Can we apply Kadane's algorithm here?
In the algorithm we get the maximum subarray and drop to 0 when sum is negative.
Let's do something similar with maximum path, drop a negative subtree to 0.

To return this root's max path, we compare the max:
1. left subtree + root
2. right subtree + root
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = -math.inf

        def helper(root):
            nonlocal global_max
            if not root:
                return 0
            
            # Post-order traversal & Kadane's algorithm (set negative to 0)
            left_max = max(0, helper(root.left))
            right_max = max(0, helper(root.right))

            # Update if this path is new global max
            path_sum = left_max + right_max + root.val
            global_max = max(global_max, path_sum)

            # Return the largest path: root + left vs root + right
            return root.val + max(left_max, right_max)

        helper(root)
        return global_max