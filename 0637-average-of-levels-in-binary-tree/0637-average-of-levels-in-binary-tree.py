# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = deque()
        q.append(root)
        visited = set()
        averages = []
        
        while q:
            size = len(q)
            total, count = 0, 0
            for idx in range(size):
                node = q.popleft()
                total += node.val
                count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            averages.append(total/count)
        

        return averages
            
        
            
                
            
            
            
            
            