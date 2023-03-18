# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def add(q, y_levels):
            q = [(node.val, y_idx) for node, y_idx in q]
            q.sort()
            for node, y_idx in q:
                y_levels[y_idx].append(node)
            
        q = deque()
        q.append((root,0))
        y_levels = defaultdict(list)
                 
        while q:
            #add
            add(q, y_levels) 
                 
            #process     
            size = len(q)
            for idx in range(size):
                node, y_idx = q.popleft()
                if node.left:
                    q.append((node.left, y_idx - 1))
                if node.right:
                    q.append((node.right, y_idx + 1))
                 
        y_keys = list(y_levels.keys())
        y_keys.sort()
        result = []
        for key in y_keys:
            values = y_levels[key]
            result.append(values)
            
        return result
            
            
                 
                 
            
        