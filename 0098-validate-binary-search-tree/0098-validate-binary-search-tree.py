# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, min_, max_):
            
            if not root:
                return True
            
            if not (min_ < root.val < max_):
                return False
            
            return helper(root.left, min_ , root.val) and helper(root.right, root.val, max_)
            
        return helper(root, float('-inf'), float('inf'))
            