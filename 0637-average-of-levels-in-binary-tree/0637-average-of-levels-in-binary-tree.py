# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = deque()
        q.append([root, 0])
        visited = set()
        totals = defaultdict(list)
        
        while q:
            node, level = q.popleft()
            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level + 1])
    
            curr = totals.get(level, [0,0])
            totals[level] = [curr[0] + node.val , curr[1] + 1]
        
        averages = []
        for level in totals:
            total, amount = totals[level]
            averages.append(total / amount)
        
        return averages
            
        
            
                
            
            
            
            
            