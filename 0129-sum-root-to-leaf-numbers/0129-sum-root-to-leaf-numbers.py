# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        
        def dfs(root, curr):
            nonlocal total
            
            if root == None:
                return 
            
            if root.left == None and root.right == None:
                curr.append(f'{root.val}')
                total += int(''.join(curr))
            
            dfs(root.left, curr + [f'{root.val}'])
            dfs(root.right, curr + [f'{root.val}'])
            
            return 
        
        dfs(root, [])
        
        return total
            
            
            