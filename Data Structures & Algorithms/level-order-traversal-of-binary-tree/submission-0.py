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

        # simple BFS - O(N) time, O(N / 2) = O(N) space
        # deque() is a python doubly linked list queue
        queue = collections.deque()
        queue.append(root)

        result = []
        while len(queue):
            level = []
            children = []
            for _ in range(len(queue)):
                # use popleft to get level from left to right
                node = queue.popleft()
                level.append(node.val)
                # add children to traverse for next level
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            result.append(level)
            queue.extend(children)
        return result
