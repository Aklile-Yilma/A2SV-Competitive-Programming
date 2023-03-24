# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        
        def helper(root, val):
    
            if root == None:
                return TreeNode(val)
            
            if  val < root.val:
                root.left = helper(root.left, val)
            else:
                root.right = helper(root.right, val)
            
            return root
                
        root = TreeNode(preorder[0])
        
        for idx in range(1, len(preorder)):
            helper(root, preorder[idx])
        
        return root