# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        q.append(root)
        
        answer = []
        
        while q:
            size = len(q)
            curr_level = []
            
            for idx in range(size):
                curr_node = q.popleft()
                if curr_node:
                    curr_level.append(curr_node.val)
                    q.append(curr_node.left)
                    q.append(curr_node.right)
        
            if curr_level:
                answer.append(curr_level)
                    
        return answer
            
            