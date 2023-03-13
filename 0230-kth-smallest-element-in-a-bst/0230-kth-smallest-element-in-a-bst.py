# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def helper(root, arr, k):
            if root == None:
                return []
            
            if len(arr) >= k:
                return 
            
            return helper(root.left, arr, k) + [root.val] + helper(root.right, arr, k) 
          
        arr = helper(root, [], k)
        
        return arr[k-1]

        
        
      
        
        
        