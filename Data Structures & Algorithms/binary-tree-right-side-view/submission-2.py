# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Solution: level-order traversal (BFS) and only print the right-side of the level
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            
            node = None
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # last node that was popped is the right-most node of the level
            result.append(node.val)

        return result
            