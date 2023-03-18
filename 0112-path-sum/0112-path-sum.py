# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        hasSum = False
        
        def backtrack(root, curr_sum):
            nonlocal hasSum
            
            if root == None:
                return 
            
            if root.left == None and root.right == None:
                curr_sum += root.val
                
                if curr_sum == targetSum:
                    hasSum = True
                return 
            
            backtrack(root.left, curr_sum + root.val)
            backtrack(root.right, curr_sum + root.val)
            
            return
            
        backtrack(root, 0)
        
        return hasSum
                
        