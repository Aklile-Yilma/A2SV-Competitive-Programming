# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque()
        q.append(root)
        right_side = []
        
        while q:
            size = len(q)
            level = []
            
            for idx in range(size):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if level:
                right_side.append(level[-1])
                
        return right_side
                
                    
            
        