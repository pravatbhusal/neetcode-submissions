# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Similar Problem: "Construct Binary Tree from Preorder and Inorder Traversal"
In this problem, we were given the preorder and inorder traversal lists and converted it into a binary tree.
We can do the reverse, convert the tree node into a preorder/inorder traversal stringified lists.

We can actually serialize/deserialize using only the preorder traversal. If we know when a node is NULL, then
we can reconstruct the tree from only the preorder traversal.

Example from Leetcode diagram input: [1, 2, 3, null, null, 4, 5]
Here's the preorder traversal list: [1, 2, null, null, 3, 4, null, null, 5, null, null]
In deserialize, Use a global index i to track our position in the preorder list across recursive calls.
"""
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []

        def helper(node):
            if not node:
                preorder.append("N")
                return None
            preorder.append(str(node.val))
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return ",".join(preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(",")

        i = 0
        def helper():
            nonlocal i
            node_i = preorder[i]
            i += 1
            if node_i == "N":
                return None
            node = TreeNode(int(node_i))
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()