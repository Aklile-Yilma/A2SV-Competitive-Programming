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
                return
            
            if  val < root.val and root.left == None:
                root.left = TreeNode(val)
                return
            
            if  val > root.val and root.right == None:
                root.right = TreeNode(val)
                return
            
            #recursive call
            if val < root.val:
                return helper(root.left, val)
            else:
                return helper(root.right, val)
                
            
        root = TreeNode(preorder[0])
        
        for idx in range(1, len(preorder)):
            helper(root, preorder[idx])
        
        return root