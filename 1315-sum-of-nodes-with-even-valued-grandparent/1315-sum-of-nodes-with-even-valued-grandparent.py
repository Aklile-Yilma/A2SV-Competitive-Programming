# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        total = 0
        def dfs(g_parent, parent, root):
            nonlocal total
            if root == None:
                return
            
            if g_parent and g_parent % 2 == 0:
                total += root.val
                
            dfs(parent, root.val, root.left)
            dfs(parent, root.val, root.right)
            
            return
        
        dfs(None, None, root)
        
        return total
            
        