# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # since we're inverting by level, BFS seems viable
        # just flip the right nodes with the left nodes
        bfs = deque()
        bfs.append(root)

        while len(bfs):
            node = bfs.popleft()

            # flip
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        return root

