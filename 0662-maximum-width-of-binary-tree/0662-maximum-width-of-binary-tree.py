# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            
        width = 1
        queue = deque()
        queue.append((root, 1))
        
        while queue:
            size = len(queue)
            for idx in range(size):
                node, pos = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*(pos)))
                if node.right:
                    queue.append((node.right, 2*(pos)+1))

            if queue:
                width = max(width, queue[-1][1] - queue[0][1] + 1)
            
        return width
    
        