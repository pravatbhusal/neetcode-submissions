# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # preorder traversal is always the root of a subtree
    # so create a node from the preorder traversal
    # [1, 2, 3, 4]

    # in order traversal gives us the tree's traversal in order (left to right)
    # [2, 1, 3, 4] <- notice the mid value is the subtree's root.
    # 1 is the root of 2 and 3, 3 is the root of 4

    # Solution: use the node from preorder then check the left and right of middle in inorder list.
    # get the node's index in the inorder list and get mid - 1 (left) and mid + 1 (right).

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = preorder[0]

        # find the root's index from inorder list, which is in middle of left and right
        mid = inorder.index(root)
        root_node = TreeNode(root)

        # left subtree is mid - 1 from inorder list
        # slice the lists before mid
        root_node.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # right subtree is mid + 1 from inorder list
        # slice the lists after mid
        root_node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root_node
        
        

