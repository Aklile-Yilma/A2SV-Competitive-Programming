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
            curr_level = []
            for idx in range(size):
                node = q.popleft()
                curr_level.append(node.val) 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            averages.append(sum(curr_level)/len(curr_level))
        

        return averages
            
        
            
                
            
            
            
            
            