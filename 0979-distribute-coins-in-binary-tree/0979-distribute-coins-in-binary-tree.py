# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        mov = 0
        def dfs(node):
            
            nonlocal mov
            if node == None:
                return 0
            
            right = dfs(node.right) 
            left = dfs(node.left)
            mov += abs(right) + abs(left)
            return node.val - 1 + right + left
                       
                       
        dfs(root)
        return mov  
            