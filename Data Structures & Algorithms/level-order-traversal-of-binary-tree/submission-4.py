# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        # BFS - breadth first search
        while queue:
            level_count = len(queue)
            level = []
            for i in range(level_count):
                # pop the node from this level
                node = queue.popleft()
                level.append(node.val)

                # queue the node's children to the end of the queue
                # it will be processed in the next loop
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)

        return result