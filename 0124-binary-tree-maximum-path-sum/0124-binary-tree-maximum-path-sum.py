# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = root.val
        
        def dfs(root):
            nonlocal max_sum
            
            if root == None:
                return 0
            
            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))
            
            #max sum with splitting
            max_sum = max(max_sum, root.val + left_max + right_max)
            #without splitting
            return root.val + max(left_max, right_max)
            
        dfs(root)
        
        return max_sum
            
        